print 'Hello world'

print 'What is your name?'
name = str(raw_input('>>'))
print ''

print 'Nice!!'
print ''

print 'So %s we will guess your age now' % str(name)

print 'what is your first number of your age?'
first_number = int(raw_input('>>'))
print ''

number1 = first_number * 5
print 'Ok, %s, I will multiply that number with 5 - %s' % (str(name), str(number1))
print ''

number2 = number1 + 3
print 'Ok, %s, I will add 3 to the result - %s' % (str(name), str(number2))
print ''

number3 = number2 * 2
print 'Ok, %s, I will double the result - %s' % (str(name), str(number3))
print ''

print 'Now I need the second number of your age'
second_number = int(raw_input('>>'))
print ''

number4 = number3 + second_number
print 'now, %s, I will add the second number with the current result %s - %s' % (str(name), str(number3), str(number4))
print ''

your_age = number4 - 6
print 'now, %s, I will substract 6 from the result and voila!! Your age is - %s' % (str(name), str(your_age))
print ''
