# 1- Create a text file called countvowels.py

# 2- Inputs a word (a string)

# 3- Counts how many vowels are in the word Tip: You can scroll through every character of a string using its index. For example, if word = 'hello' then word[0] is the letter h and word[1] is the letter e. Use the len() function to find the length of a string. For example, in the above example, len(word) is 5. Use simple if statement/s to detect if the character is 'a', 'e', 'i', 'o' or 'u' Every time you find a vowel you must increase a counter (an integer variable) In the next chapter (Lists) you'll discover a much easier way of performing this task.

# 4- Save and run

word = input("Input a word: ")
wordLength = len(word)
# word = "number of vowels in a String in Python"

# initializing count variable
count = 0

# declaring a variable for index
i = 0

for i in range(wordLength):
    if (
        (word[i] == "a")
        or (word[i] == "e")
        or (word[i] == "i")
        or (word[i] == "o")
        or (word[i] == "u")
    ):
        count += 1

print("Number of vowels found: ",count)

