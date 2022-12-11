# 1. Write a python script to create a String in 3 different possible ways
a = 'Aman'
b = "Dwivedi"
c = """AMAN DWIVEDI"""
d = '''aman dwivedi'''
e = "'Aman'"

print(a, b, c, d, e, sep='\n')

# 2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
s = "iNeuron"

print(s)

s1 = s[5:]
print(s1)

# 3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)

s = "Hello Learners"
print(s)
print(s[2:5])

# 4. Write a python script to demonstrate String Concatenation adding space in between (Given Strings a=”Learning” b=”Python” )

a = "Learning"
b = "Python"

c = ' '.join([a, b])

print(a)
print(b)
print(c)

# 5. Write a python script to get the count of total number of characters in String a=“iNeuron”
s = "iNeuron"

print(len(s))

# 6. Write a python script to reverse a String. (“iNeuron”)

s = "iNeuron"

print(s[::-1])

# 7. Write a python script to determine whether a string contains a specific substring.

str = "abcstrsbcabc"

a = False

if 'abcd' in str:
    print('substring is present')
else:
    print('substring is not present')

# 8. Write a python script to check if a string contains only numbers.

str = input('Enter any string : ')

print("The string is number : ",str.isdigit())

# 9. Write a python script to check if a string contains only characters of the alphabet.

str = input('Enter any string : ')

print('String contains only characters of the alphabet :', str.isalpha())

# 10. Write a python script to convert an integer to a string.
s = int(input('Enter a number : '))

print(type(s))

s = str(s)

print(type(s))