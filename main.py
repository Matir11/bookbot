#!/usr/bin/env python3

file_path = "/workspaces/bookbot/github.com/matir11/bookbot/books/frankenstein.txt"
def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = file_contents.split()
    count = len(words)
    return count

# word_count = count_words(file_path)
# print(word_count)

def character_count(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    letters = {}
    lowercase = file_contents.lower()
    for character in lowercase:
        if character.isalpha():
            letters[character] = letters.get(character, 0) + 1  
    return letters
        

count_characters = character_count(file_path)
# print(count_characters)

count_characters.sort()
print(count_characters)

# def character_sort(count_characters):
