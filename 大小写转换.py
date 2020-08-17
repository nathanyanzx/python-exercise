import string
a=str(input())
for i in a:
    if i in string.ascii_lowercase:
        print(i.upper(),end='')
    elif i in string.ascii_uppercase:
        print(i.lower(),end='')


