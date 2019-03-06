def main():
    user_input = int(raw_input('Pick a number: '))
    # if 13 > 5:
    #   print "13 is greater than 5"

    if user_input > 5:
        print "%s is greater than 5" % str(user_input)
    else:
        print "%s is not greater than 5" % str(user_input)
        

if __name__ == '__main__':
    main()
