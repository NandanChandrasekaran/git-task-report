from formula_task1_Q2 import Sort 
class Search:
    def binary_search(self,L,target):
        low=0
        high=len(L)-1
        while low<=high:
            middle=(high+low)//2

            if L[middle]==target:
                return middle
            elif L[middle]>target:
                high=middle-1
            else:
                low=middle+1

     







sorter=Sort()
L=sorter.selection_sort()
print("Sorted list :",L)


target=input("Enter a string to find : ")
searcher=Search()
y=searcher.binary_search(L,target)

if y==-1:
    print("String not found")
else:
    print("String found at index:",y)

        


        


