def reverseString(mystr):
    reverse = Stack()
    revstr = ""
    for letter in mystr:
        reverse.push(letter)
    for letter in mystr:
        revstr += reverse.pop()
    return revstr

print(reverseString("apple"))
