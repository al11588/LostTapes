def reversefunction(str1): #the function to reverse the string

    stringstuff = ''
    index = len(str1)
    while index > 0:
        stringstuff += str1[ index - 1 ]
        index = index - 1
    return stringstuff

def fizzbuzzfunction(n):#the function to do fizz buzz

    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    else:
        return str(n)

print(reversefunction('alvin lawson'))
print "\n".join(fizzbuzzfunction(n) for n in xrange(1, 101))
