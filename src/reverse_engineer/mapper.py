def generate_block_diagram(modules):
    """
    Groups modules by top-level package and creates cross-package flowchart links.
    """
    packages = {}
    # Valid local packages to draw dependencies between
    local_packages = ('centrality', 'hubs', 'bugs', 'suggestions', 'agent', 'reverse_engineer')
    
    for mod_name, mod_info in modules.items():
        parts = mod_name.split('.')
        pkg = parts[0]
        if pkg not in packages:
            packages[pkg] = set()
            
        for imp in mod_info['imports']:
            imp_parts = imp.split('.')
            imp_pkg = imp_parts[0]
            if imp_pkg != pkg and imp_pkg in local_packages:
                packages[pkg].add(imp_pkg)
                
    mermaid_lines = ["graph TD"]
    for pkg in sorted(packages.keys()):
        # Capitalize label for display
        label = pkg.replace('_', ' ').capitalize()
        mermaid_lines.append(f"    {pkg}[\"{label} Package\"]")
        
    for pkg, deps in sorted(packages.items()):
        for dep in sorted(list(deps)):
            mermaid_lines.append(f"    {pkg} --> {dep}")
            
    return "\n".join(mermaid_lines)

def generate_oop_diagram(classes):
    """
    Constructs class definitions, methods, inheritance, and compositions in Mermaid classDiagram format.
    """
    mermaid_lines = ["classDiagram"]
    
    for class_name, class_info in sorted(classes.items()):
        mermaid_lines.append(f"    class {class_name} {{")
        for method in sorted(class_info['methods']):
            # Filter private methods for clean diagrams
            if not method.startswith('__'):
                mermaid_lines.append(f"        +{method}()")
        mermaid_lines.append("    }")
        
    for class_name, class_info in sorted(classes.items()):
        for base in class_info['bases']:
            if base in classes:
                mermaid_lines.append(f"    {base} <|-- {class_name} : Inheritance")
                
        for comp in class_info['compositions']:
            if comp in classes:
                mermaid_lines.append(f"    {class_name} *-- {comp} : Composition")
                
    return "\n".join(mermaid_lines)
