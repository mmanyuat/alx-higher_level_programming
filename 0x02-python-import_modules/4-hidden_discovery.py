#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get the names defined in the module
    names = dir(hidden_4)

    # Filter out names starting with '__'
    filtered_names = [name for name in names if not name.startswith("__")]

    # Sort and print each name
    for name in sorted(filtered_names):
        print(name)
