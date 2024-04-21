#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, sys.argv[1]))
    elif argc > 1:
        print("{} arguments:".format(argc)) 
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
