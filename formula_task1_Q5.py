def hash_table():
    x=int(input("How many numbers would you like to hash: "))
    numbers=[]
    for i in range(x):
        y=int(input("Enter number:"))
        numbers.append(y)
    hash_table=[[],[],[],[],[],[],[],[],[],[],[]]

    for n in numbers:
        index=n%10
        hash_table[index].append(n)
    return hash_table


result=hash_table()
print(result)