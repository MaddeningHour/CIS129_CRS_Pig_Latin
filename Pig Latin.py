#Christopher Robles Serrano
#Pig Latin Extra Credit
#12/3/24
#This programs converts user phrases into pig latin.

def pigLatinTranslator():
    #Getting inputs converting into a list using the .split() method.
    myPhrase = input("Enter a phrase to convert to pig latin: ").split()

    #Our vowels to check if a word begins with a vowel or no
    myVowels = 'aeiou'

    #Creating an empty list to append our translated words
    myPigLatin = []

    for word in myPhrase:
        #Checking if the first letter of a word is a vowel. If so just add 'ay' to the end of the word and append to our list.
        if word[0].lower() in myVowels:
            myPigLatin.append(word + 'ay')

        #Else append the word starting at the second letter(index 1) add the first letter(index 0) to the end and add 'ay'
        else:
            myPigLatin.append(word[1:] + word[0] + 'ay')

    #Converting our list of translated words into a string using the " ".join() method. The empty space seperates the words.    
    myPigLatin = " ".join(myPigLatin)

    #Printing our phrase
    print(f'Your translated sentence is: "{myPigLatin}"')

    #Loop over if the user wants to enter a new phrase.
    again = input("Enter in a new phrase? (y or n)").lower()
    if again == 'y':
        pigLatinTranslator()

pigLatinTranslator()