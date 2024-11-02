#!/usr/bin/python
import json
import os
import sys
import time
from pprint import pprint
import traceback
from mock_module_strings import _bootstrap
from node_builtins import _console

import STPyV8

module_cache = {}

def execute(path):
    with STPyV8.JSContext() as ctx:
        # Read the content of the file
        with open(path, 'r') as file:
            code = file.read()
        ctx.locals.console = _console()
        # Wrap the code in an IIFE
        wrapped_code = f"{_bootstrap} {code}"
        
        try:
            # Execute the JavaScript code
            ctx.eval(wrapped_code)
        except Exception as e:
            print(f"Error executing JavaScript code: {e}")
            traceback.print_exc()  # Print the full stack trace
        print("donesky")
        print(dir(ctx.locals))
        print(dir(ctx.locals.document))
        print(dir(ctx.locals.document.body))
        print(dir(ctx.locals.document.innerHTML))



def get_entry_point(project_dir):
    bundle_js_path = os.path.join(project_dir, 'dist', 'bundle.js')
    if os.path.isfile(bundle_js_path):
        return bundle_js_path
    
    index_js_path = os.path.join(project_dir, 'index.js')
    if os.path.isfile(index_js_path):
        return index_js_path
    
    package_json_path = os.path.join(project_dir, 'package.json')
    if os.path.isfile(package_json_path):
        with open(package_json_path, 'r') as f:
            package_json = json.load(f)
            main_file = package_json.get('main')
            if main_file:
                main_file_path = os.path.join(project_dir, main_file)
                if os.path.isfile(main_file_path):
                    return main_file_path
    return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        provided_path = sys.argv[1]
        abs_path = os.path.abspath(provided_path)
        if provided_path.endswith('.js') and os.path.isfile(provided_path):
            js_file_path = abs_path
            project_dir = os.path.dirname(js_file_path)
        else:
            project_dir = abs_path
            js_file_path = get_entry_point(project_dir)
            if js_file_path is None:
                print("Error: No valid entry point found (bundle.js, index.js, or package.json with main field).")
                sys.exit(1)
    else:
        print("Error: Please provide a valid .js file path or directory.")
        sys.exit(1)
    
    os.chdir(project_dir)
    execute(js_file_path)