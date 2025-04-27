import ast

def analyze(code):
    try:
        tree = ast.parse(code)
        return {
            "valid": True,
            "metrics": {
                "line_count": len(code.splitlines()),
                "function_count": len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
            },
            "comments": "No issues found."
        }
    except Exception as e:
        return {
            "valid": False,
            "error": str(e),
            "comments": f"Syntax error detected: {e}"
        }