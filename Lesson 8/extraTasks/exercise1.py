word1 = input("Enter a word ")
word2 = input("Enter another word ")
if len(word1) == len(word2):
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    print(sorted_word1)
    print(sorted_word2)
    if sorted_word1 == sorted_word2:
        print(f"{word1} and {word2} are anagrams")
else:
    print(f"{word1} and {word2} are not anagrams")