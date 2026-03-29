paragraph = input("Enter a paragraph: ") # User enters a paragraph

cleanParagraph = [] # Array that stores the individual words
frequency = {} # Dictionary that stores the words and their frequency

string = "" # Making the string empty

for i in range(len(paragraph)): # Looping through depending on length of paragraph
    # Running if the current char is an alphabet
    if paragraph[i].isalpha():
        string += paragraph[i].lower() # Adding this char converted to lowecase to string
    # Running if the current char is not an alphabet
    else: 
        # Adding the string to cleanParagraph and resetting string if string is empty
        if string != "":
            cleanParagraph.append(string)
            string = ""

    # Adding the string to cleanParagraph if i has reached the length of paragraph and string isn't empty
    if i+1 == len(paragraph):
        if string != "":
            cleanParagraph.append(string)

# Creating a dictionary for each word, word : frequency
for word in cleanParagraph:
    # If the word already exists, append the frequency
    if word in frequency:
        frequency[word] += 1
    # If the word does not exist, make the frequency 1
    else:
        frequency[word] = 1

# Outputting stats: total words, total unique words
print("Total words:", len(cleanParagraph))
print("Total unique words: ", len(frequency))

# Outputting the word and its frequency in terms of bars
for key, value in frequency.items():
    print(key, ("⬜" * value))