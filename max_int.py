#User repeatedly inputs a number until a negative value is entered,
#print the Max input
num_int = int(input("Input a number: "))
max_num = num_int
while num_int >= 0:
    if num_int > max_num:
        max_num = num_int
    
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)