def hash_table():
    x=int(input("How many numbers would you like to hash: "))
    numbers=[]
    for i in range(x):
        y=int(input("Enter number:"))
        numbers.append(y)
    hash_table=[[],[],[],[],[],[],[],[],[],[],[]]

    for n in numbers:
        index=n%10
        sublist=hash_table[index]

        low=0
        high=len(sublist)
        while low<high:
            mid=(low+high)//2
            if sublist[mid]<n:
                low=mid+1
            else:
                high=mid

        sublist.insert(low,n)


    return hash_table


result=hash_table()
print(result)