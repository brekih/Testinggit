#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#Make sure that you write up the algorithm before starting to code.
#Then implement the algorithm in Python. 
#Put your algorihmic description as a comment in the program file.
n = int(input("Enter the length of the sequence: ")) # Do not change this line
counter = 1
n1 = 1
n2 = 2
n3 = 3
print(n1)
print(n2)
print(n3)
while counter <= n -3:
    n4 = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = n4
    counter += 1
    print(n4)


    
    