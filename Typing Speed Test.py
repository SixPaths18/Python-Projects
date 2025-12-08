import random, time

# List of random sentences that user types
sentences = [
    "Learning Python can be both fun and challenging, but the rewards are absolutely worth the effort.",
    "Sometimes the smallest step in the right direction ends up being the biggest step of your life.",
    "Creativity is intelligence having fun, and it often comes from experimenting without fearing mistakes.",
    "The most important thing is to never stop questioning, because curiosity drives real understanding.",
    "Success is not final, failure is not fatal, it is the courage to continue that truly matters.",
    "Even when things seem impossible, persistence and hard work can create extraordinary outcomes.",
    "Reading books allows us to travel to different worlds, meet new people, and explore endless ideas.",
    "A positive attitude, combined with consistent effort, can turn seemingly ordinary days into extraordinary ones.",
    "Time spent improving yourself is never wasted, because growth leads to opportunities that last a lifetime.",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful."
]

# Random sentence the user types
sentence = random.choice(sentences)

# Stating rules for user
print("Press enter once done typing.")
print("The sentence is:")
print(sentence)


input("Press enter to start typing: ")
start = time.time() # Starting timer once user presses a key
typed = input()
end = time.time() # Ending timer when user presses enter

timeTaken = end-start

# Function to check accuracy
def accuracy():
    count = 0

    # Splitting words in each sentences
    targetSentence = sentence.split()
    typedSentence = typed.split()

    total = len(targetSentence) # Total words in sentence

    smallest = targetSentence if len(targetSentence) < len(typedSentence) else typedSentence # Finding the smallest sentence

    # Finding the amount of words correct
    for i in range(len(smallest)):
        if typedSentence[i] == targetSentence[i]:
            count += 1

    # Calculating wpm and accurate
    wpm = (count/timeTaken) * 60
    accurate = (count/total) * 100

    # Output
    print(f"Words Per Minute (WPM): {wpm:.2f}")
    print(f"Accuracy: {accurate:.0f}%")

accuracy()