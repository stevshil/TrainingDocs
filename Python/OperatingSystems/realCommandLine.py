import getopt
import sys
import fileinput

def usage():
    print("{argv[0]} [-hv][-o output][--help][--output=something] [fileargs...]")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:ho:v", ["search","help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
            print("Am I shouting? ",verbose)
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
            print(output)
        elif o in ("-s", "--search"):
            findword = a
            print(findword)
        else:
            assert False, "unhandled option"

    for file in fileinput.input(args):
                if findword in file:
                    print('{}: {}'.format(fileinput.filename(), file), end=' ')

if __name__ == "__main__":
    main()