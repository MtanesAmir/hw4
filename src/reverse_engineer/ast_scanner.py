import os
import ast

class ASTScanner:
    def __init__(self, target_dir: str):
        self.target_dir = os.path.abspath(target_dir)
        self.classes = {}
        self.modules = {}

    def scan(self):
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.target_dir)
                    # Convert file path to module name format: package.submodule
                    module_name = rel_path[:-3].replace(os.sep, '.')
                    
                    try:
                        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                            node = ast.parse(f.read(), filename=full_path)
                        self.scan_file_node(node, module_name, rel_path)
                    except Exception:
                        pass

    def scan_file_node(self, node, module_name, rel_path):
        self.modules[module_name] = {
            'imports': [],
            'classes': [],
            'file': rel_path
        }
        
        for subnode in ast.walk(node):
            # Track imports
            if isinstance(subnode, ast.Import):
                for alias in subnode.names:
                    self.modules[module_name]['imports'].append(alias.name)
            elif isinstance(subnode, ast.ImportFrom):
                if subnode.module:
                    self.modules[module_name]['imports'].append(subnode.module)
                    
            # Track classes
            elif isinstance(subnode, ast.ClassDef):
                class_name = subnode.name
                self.modules[module_name]['classes'].append(class_name)
                
                bases = []
                for base in subnode.bases:
                    if isinstance(base, ast.Name):
                        bases.append(base.id)
                    elif isinstance(base, ast.Attribute):
                        bases.append(base.attr)
                        
                methods = [n.name for n in subnode.body if isinstance(n, ast.FunctionDef)]
                
                # Check for compositions inside class body
                compositions = []
                for class_subnode in ast.walk(subnode):
                    if isinstance(class_subnode, ast.Assign):
                        for target in class_subnode.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                                if isinstance(class_subnode.value, ast.Call) and isinstance(class_subnode.value.func, ast.Name):
                                    func_name = class_subnode.value.func.id
                                    # Class initialization heuristic (starts with uppercase)
                                    if func_name[0].isupper() and func_name not in compositions:
                                        compositions.append(func_name)
                                        
                self.classes[class_name] = {
                    'bases': bases,
                    'methods': methods,
                    'compositions': compositions,
                    'module': module_name,
                    'file': rel_path
                }
