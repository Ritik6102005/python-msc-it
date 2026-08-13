paragraph = input("Enter a paragraph: ")

words = paragraph.split()

total_words = len(words)
unique_words = len(set(words))

longest_word = max(words, key=len)
shortest_word = min(words, key=len)

print("\n--- Result ---")
print("Total number of words:", total_words)
print("Number of unique words:", unique_words)
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)

print("Words appearing more than once:")

for word in set(words):
    if words.count(word) > 1:
        print(word)
