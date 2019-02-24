# Function

#def print_name(name):
 #   print name

#print_name('aritra')
 
def print_name(name = 'aritra', age = 29):
    """
    This function will print a name

    Args: name= a string representing name
    age = the person's age

    Returns = String
    """
    print name

    return 'My name is %s, my age is %s' % (str(name), str(age))

st1 = print_name()
print st1

st2 = print_name('pal', 25)
print st2
