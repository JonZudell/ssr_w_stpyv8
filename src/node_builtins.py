def _console():
    def log(*args):
        print("LOG:", *args)
    def error(*args):
        print("ERROR:", *args)
    
    return {
        "log" : log,
        "error" : error,
    }