#Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!

hindi_dict = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "माफ़ करें": "Sorry",
    "हाँ": "Yes",
    "नहीं": "No",                                     
}
word = input("Enter a Hindi word to look up its English translation: ")
translation = hindi_dict.get(word)      
if translation:
    print(f"The English translation of '{word}' is: {translation}")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")        