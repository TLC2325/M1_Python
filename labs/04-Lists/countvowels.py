# Part 2

# Task 1 - Count Vowels

# 1- Create a file called countvowels.py

# 2- Inputs a word (a string)

# 3- Counts how many vowels are in the word Tip: You can scroll through every character of a string in the same way as you do with numbers in a range() function. Use a simple if statement/s to detect if the character is 'a', 'e', 'i', 'o' or 'u' Every time you find a vowel you must increase a counter (an integer variable) Or (better), you may consider using the 'in' keyword

# 4- Save and run
word = input("Enter a word: ")
word = word.lower()
counter = 0

for character in word:
    if (
        character == "a"
        or character == "e"
        or character == "i"
        or character == "o"
        or character == "9"
    ):
        counter += 1

print("There are",counter,"vowel(s) in your word.")
