# Dorlens Janvier Chapter5 Exercises 1

number = [1,2,3,3,4,5,3,6,7,8,9,10]


print(number)


def calMedian(number):
        number.sort()
        if len(number) % 2 == 0:
            length = len(number)
        if length % 2 == 0:
            median = number[length//2] + number[length//2-1]/2
        else :
            median = number[length//2]

        return median

def calcNumber(number):
     return sum(number)/len(number)

def calcMode(number):
    if not number:
        return 0
    max_count = 0
    mode = None
    for i in number:
        count = number.count(i)
        if count > max_count:
            max_count = count
            mode = i
    return mode





def main(): 

 print("inside main")
 print("Median:", calMedian(number))
 print("Average:", calcNumber(number))
 print("mode" , calcMode (number))
 
main()
