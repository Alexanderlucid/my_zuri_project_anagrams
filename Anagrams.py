# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
def find_anagrams():
    # [assignment] Add your code here
    word1 = input("Enter your first word: ")
    if type(word1) == str:
        word2 = input("Enter another word: ")
        if type(word2) == str:
            if(sorted(word1)== sorted(word2)):
                print("True.")
            else:
                print("False.")
                    
        else:
            print("This is not a word")
    else:
        print("This is not a word")
    


find_anagrams()