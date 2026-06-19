import os
import re

def refactor_file(file_path, bug_type):
    """
    Applies automated refactoring modifications to a source file based on bug category.
    Returns (success, original_content_or_error_msg).
    """
    if not os.path.exists(file_path):
        return False, f"File not found: {file_path}"
        
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()
        
    original = code
    modified = False
    
    clean_bug = bug_type.lower()
    
    if 'waiting' in clean_bug or 'timeout' in clean_bug:
        # 1. requests.get/post/put/delete
        requests_pat = r'\brequests\.(get|post|put|delete)\(([^)]*?)\)'
        def repl_requests(match):
            func = match.group(1)
            args = match.group(2).strip()
            if 'timeout' not in args:
                comma = ', ' if args else ''
                return f"requests.{func}({args}{comma}timeout=10)"
            return match.group(0)
            
        code, count = re.subn(requests_pat, repl_requests, code)
        if count > 0:
            modified = True
            
        # 2. urllib.request.urlopen or urlopen
        urllib_pat = r'\burlopen\(([^)]*?)\)'
        def repl_urllib(match):
            args = match.group(1).strip()
            if 'timeout' not in args:
                comma = ', ' if args else ''
                return f"urlopen({args}{comma}timeout=10)"
            return match.group(0)
            
        code, count = re.subn(urllib_pat, repl_urllib, code)
        if count > 0:
            modified = True
            
    elif 'retry' in clean_bug or 'retries' in clean_bug:
        # Refactor while True: try... except: loops to bounded retry loops
        while_pat = r'while\s+True\s*:\s*\n(\s+)try\s*:'
        def repl_while(match):
            indent = match.group(1)
            parent_indent = indent[:-4] if len(indent) >= 4 else ''
            return f"_retries = 0\n{parent_indent}while _retries < 3:\n{indent}try:"
            
        code, count = re.subn(while_pat, repl_while, code)
        if count > 0:
            modified = True
            
            # Insert _retries increment and backoff time.sleep in except block
            except_pat = r'(\s+)except(\s+Exception)?\s*:'
            def repl_except(match):
                ind = match.group(1)
                return f"{match.group(0)}\n{ind}    _retries += 1\n{ind}    import time\n{ind}    time.sleep(1)"
            code, _ = re.subn(except_pat, repl_except, code)
            
    elif 'local state' in clean_bug or 'sticky session' in clean_bug or 'session' in clean_bug:
        # Replace local dict session stores with redis cache
        session_pat = r'(\bself\.sessions?|\bsessions?)\s*=\s*\{\s*\}'
        def repl_session(match):
            var_name = match.group(1)
            return f"import redis\n{var_name} = redis.Redis(host='localhost', port=6379, db=0)"
        code, count = re.subn(session_pat, repl_session, code)
        if count > 0:
            modified = True
            
    elif 'syntax' in clean_bug or 'compilation' in clean_bug or 'defect' in clean_bug:
        new_keyword_pat = r'\bnew\s+([A-Z][a-zA-Z0-9_]*)\('
        code, count1 = re.subn(new_keyword_pat, r'\1(', code)
        if count1 > 0:
            modified = True
            
        print_pat = r'\bprint\s+"([^"]*)"'
        code, count2 = re.subn(print_pat, r'print("\1")', code)
        if count2 > 0:
            modified = True
            
        assignment_if_pat = r'\bif\s+([a-zA-Z0-9_]+)\s*=\s*([a-zA-Z0-9_"\']+)\s*:'
        code, count3 = re.subn(assignment_if_pat, r'if \1 == \2:', code)
        if count3 > 0:
            modified = True
            
        elseif_pat = r'\belse\s+if\s+'
        code, count4 = re.subn(elseif_pat, 'elif ', code)
        if count4 > 0:
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)
        return True, original
        
    return False, "No modifications applied"
