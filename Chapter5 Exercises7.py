#Dorlens Janvier Chapter 5 Exercises 7 
fileName = input('Enter fileName: ')
sortedString = ''.join(sorted(fileName))
with open (fileName, 'r') as f:
 lines = f.read()
 words = lines.split()
 uniqueWords = set()

for word in words:
    uniqueWords.add(word)
sortedUniqueWords = sorted(uniqueWords)

print("Sorted unique words:")
for word in sortedUniqueWords:
    print(word)