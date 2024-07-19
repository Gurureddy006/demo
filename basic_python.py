# Reversing the string and checking if it is a pallindrom
string = "AmMa"
string = string.lower()
new_string = string[::-1]

print("Reverse of string is",new_string)

if string == new_string:
    print(string, "is a pallindrome")