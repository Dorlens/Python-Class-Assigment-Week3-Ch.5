# Dorlens Janvier Chapter 5 Exercises 2

fileName = input("Enter a file name: ")
with open(fileName, 'r' ) as f:
 lines = f.readlines()

while True:
     print("number of lines in this file" , len(lines))
     lineNumber = ("Enter line Number(Press 0 to quit): ")
     if lineNumber == 0:
      print("Exiting the program.....")
      break
     if 1 <= lineNumber <= len(lines):
      print("line", lineNumber, ":" , lines[lineNumber -1])
     else:
       print("invalid line number please enter a number between 1",len(lines))
   
