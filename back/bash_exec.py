import os

def main():
    bashCommand = "pyreverse -o png __init__.py ."
    #bashCommand = "pyreverse -o puml __init__.py ."

    os.system(bashCommand)

if __name__ == '__main__':
    main()
