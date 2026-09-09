# Create a class with a function that does selection sort on a list of strings.

class Sort:
    def selection_sort(self):
        L = []
        n = int(input("Enter number of strings for list: "))

        for k in range(n):
            L.append(input("Enter a string: "))

        for i in range(len(L)):
            min_index=i

            for j in range(i+1,len(L)):
                if L[j]<L[min_index]:
                    min_index = j

            temp1=L[min_index]
            temp2=L[i]
            L[i]=temp1
            L[min_index]=temp2

            

        return L

sorter=Sort()
print(sorter.selection_sort())
                

        
