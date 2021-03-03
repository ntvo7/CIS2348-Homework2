userinput = input()
userinput.replace(" ","")



def palindrome(userstr):
    return userstr == userstr[::-1]

result = palindrome(userinput)

if result:
    print(userinput, 'is a palindrome')
else:
    print(userinput, 'is not a palindrome')

