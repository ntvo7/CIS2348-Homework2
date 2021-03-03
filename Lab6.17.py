userpwd = input()
newpwd = ''
for i in userpwd:
    if i == "i":
        newpwd = newpwd + "!"
    elif i == 'a':
        newpwd = newpwd + "@"
    elif i == 'm':
        newpwd = newpwd + "M"
    elif i == 'B':
        newpwd = newpwd + "8"
    elif i == 'o':
        newpwd = newpwd + "."
    else:
        newpwd = newpwd + i
newpwd = newpwd + 'q*s'
print(newpwd)



