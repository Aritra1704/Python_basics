import third_program02

from third_program02 import print_age

def main():
    """ This is the main function """

    print "F1 executed"
    n = third_program02.print_name("Aritra")
    print n
    print print_age(29)

if __name__ == '__main__':
    main()
