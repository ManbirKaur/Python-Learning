print("Manbir Kaur")                #prints normally
print("Manbir\nKaur")               #prints a new line so that they are on two separate lines
print("Manbir \"Kaur\"")            #prints quotation mark
print("Manbir\Kaur")                #prints backslash

phrase = "Manbir Kaur"
print(phrase.lower())               #prints phrase in lowercase
print(phrase.upper())               #prints phrase in uppercase
print(phrase.isupper())             #prints true if phrase is in all uppercase otherwise false
print(phrase.upper().isupper())     #you can combine functions
print(len(phrase))                  #prints number of characters in phrase
print(phrase[0])                    #prints the first letter of the phrase
print(phrase.index("bir"))          #prints index of where this string starts
print(phrase.replace("Kaur", "K"))  #Replaces Kaur in the string with K