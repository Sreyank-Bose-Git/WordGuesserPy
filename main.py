from random import randint
import time

words = [
    "apple", "banana", "cat", "dog", "elephant", "flower", "guitar", "house", "ice", "jungle",
    "kite", "lemon", "mountain", "notebook", "ocean", "pencil", "queen", "rain", "sun", "tree",
    "umbrella", "violin", "window", "xylophone", "yogurt", "zebra", "ant", "book", "car", "desk",
    "ear", "fan", "glass", "hat", "island", "jacket", "key", "lamp", "mirror", "necklace",
    "orange", "pen", "quilt", "ring", "shoe", "table", "uniform", "vase", "whistle", "x-ray",
    "yard", "zoo", "airplane", "ball", "candle", "drum", "egg", "flag", "garden", "hill", "ink",
    "jar", "kangaroo", "ladder", "moon", "nest", "owl", "pizza", "quiet", "robot", "star",
    "telephone", "under", "vulture", "water", "xenon", "yo-yo", "zipper", "animal", "baby", "cloud",
    "dance", "engine", "forest", "grape", "horse", "idea", "jewel", "king", "lion", "music", "night",
    "octopus", "parrot", "question", "river", "snake", "tiger", "unicorn", "village", "wolf", "extra",
    "yellow", "zone" 
]

totalScore = 0
totalTime = 0

def ask():
    global totalScore, totalTime

    totalTime = time.time()

    wantToPlay = True
    while wantToPlay:

        Next = False

        
        try:
            wordIndex = randint(0, len(words) - 1)
        except:
            wantToPlay = False
            break

        word = words[wordIndex]

        letters = list(word)

        toBeRemoved = randint(0, len(letters) - 2)

        for i in range(0, toBeRemoved+1):
            index = randint(0, len(letters) - 1)
            letters[index] = '_'

        print(letters)

        while list(word) != letters:
            user = input("What do you expect (letter): ")

            
            if(len(user) > 1):
                if(user == "exit"):
                    wantToPlay = False
                    break  
                elif(user == "next"):
                    print(word)
                    Next = True
                    break
                else:
                    print("Please Type Only Character!")
                    print(letters)
                    continue
        
            index = word.find(user)

            if(index == -1):
                print("Not Found!")
                print(letters)
                continue
            
            while(letters[index]==user):
                index = word.find(user, index + 1)
                print(index)

            if(index == -1):
                print("Not Found!")
                print(letters)
                continue

            letters[index] = user

            print(letters)
        if(wantToPlay == True):
            if(Next == False):
                totalScore += 1
            else:
                words.pop(wordIndex)

ask()

totalTime = time.time() - totalTime

print("")
print("Your Score is", totalScore)
print("Your Time is", round(totalTime), "seconds")

print("")
print("Your Score per second is", totalScore / totalTime)