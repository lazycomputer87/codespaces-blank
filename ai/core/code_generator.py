def optimize_code(code, analysis):
    optimized_code = code
    if analysis.get("metrics", {}).get("function_count", 0) > 5:
        optimized_code = add_logging(code)
    return optimized_code

def add_logging(code):
    return f"""\
import logging
logging.basicConfig(level=logging.INFO)

{code}
"""