# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram (word,anagram):
    word = word.lower()
    word = word.replace(" ", "")
    word = [char for char in word]
    word = word.sort()

    anagram = anagram.lower()
    anagram = anagram.replace(" ", "")
    anagram = [char for char in anagram]
    anagram = anagram.sort()

    if word==anagram:
        return (f"{True}, {word1} and {anagram1} are anagrams of each other")

    else:
        return (f"{False}, {word1} and {anagram1} are not anagrams of each other")

print ("This is a program that checks if two words are anagrams of each other")
word1 = input("Enter your first word here: ")
anagram1 = input("Enter your second word here: ")
word=word1
anagram=anagram1
print(find_anagram (word,anagram))


