"""Module for various data extraction tasks on modules in Python. Built on top of the `inspect` library"""

import inspect

def generate_dicts(Module) -> tuple[dict, dict]:
    """
    Generate an argument count dict and function call dict for a module. 
    
    Returns 
    -------
    - `arg_dict`:  A dict with the function(s) as a key and the number of valid arguments as a set.
    - `call_dict`: A dict with the function(s) as a key and a callable as value.
    
    Both in alphabetical order.
    """
    
    arg_dict = {}
    call_dict = {}
    
    for name, obj in inspect.getmembers(Module, inspect.isfunction):
        if name.startswith("_") or name.startswith("x"):
            continue

        sig = inspect.signature(obj)
        param_count = sum(1 for p in sig.parameters.values() if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD))

        if name not in arg_dict:
            arg_dict[name] = set()
        
        arg_dict[name].add(param_count)
        call_dict[name] = obj
    
    return arg_dict, call_dict
