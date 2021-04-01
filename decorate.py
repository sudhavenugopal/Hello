def announce(f):
    def wrapper():
        print("About to run thr function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("hello, World!")

hello()