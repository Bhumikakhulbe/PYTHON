#input validation
while True:
    try:
        string=str(input("Enter a string "))
    except ValueError:
        print("Enter a string value")
        continue
    break
string1="" #an empty string is created
for i in string.split(): #the string will get splitted in words
    if i.isnumeric(): #checks if the string is a numeric value
        string1 += i + ' ' #concatenate the strings
    elif i[0] in ['a','e','i','o','u','y','A','E','I','O','U','Y']: #checks if the value is present in the given list
        if i.isupper(): #checks if the string is in upper case
            string1+= i+ 'YAY' + ' '
        else:
            string1+= i+ 'yay' + ' '
    elif i[0] and i[1] not in ['a','e','i','o','u','y','A','E','I','O','U','Y']: #checks if the value is not present in the given list
        if i.isupper():
            string1 += i[2:] +i[0] + i[1] + 'AY' + ' '
        else:
            string1 += i[2:] +i[0] + i[1] + 'ay' + ' '
    else:
        if i.isupper():
            string1 += i[1:] +i[0] + 'AY' + ' '
        else:
            string1 += i[1:] +i[0] + 'ay' + ' ' 
print(string1) #prints the final value
        
