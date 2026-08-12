text = input("Enter a Paragraph : ")

single = []
words = text.split()
duplicate = []

print("List of words :", words)

print("Number of words :-", len(words))

for word in words:
    frequency = words.count(word)
    if frequency == 1 and word not in single:
        single.append(word)

print("Total Unique words :", single)

big = words[0]

for word in words:
    if len(word) > len(big):
        big = word

print("Longest Word in Paragraph :", big)

small = words[0]

for word in words:
    if len(word) < len(small):
        small = word

print("Smallest Word in Paragraph :", small)

for word in words:
    frequency = words.count(word)

    if frequency > 1 and word not in duplicate:
        duplicate.append(word)

print("Repeated Words :-", duplicate)