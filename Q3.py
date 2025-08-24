# FIBONACII SERIES :
NUM  = int(input("Enter A Number : "))
print ("FIBONACII SERIES")
NUM1 = 0
NUM2 = 1
COUNT = 0
print (NUM1 , end = " ")
print (NUM2 , end = " ")
while COUNT < NUM :
    result = NUM1+NUM2
    print (result,end=" ")
    NUM1 = NUM2
    NUM2 = result
    COUNT = COUNT+1

