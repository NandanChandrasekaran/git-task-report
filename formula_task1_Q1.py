# version from main
#  Input an integer n, input n strings into a list. Create a dictionary where the key is an alphabet and the value is how many times it appears across all the strings. Not case sensitive. Eg for ["Formula", "Manipal"] the output looks like {'f':1, 'o':1, 'a':3 ...} 
def count_characters():
    n = int(input("Enter the number of strings: "))
    L = []
    for i in range(1, n + 1):
        L.append(input("Enter a string: "))
    for j in range(len(L)):
        L[j] = L[j].lower()
    char_count = {}
    for x in L:
        for k in x:
            if k.isalpha():
                if k in char_count:
                    char_count[k]+=1
                else:
                    char_count[k]=1
    
    sorted_char_count = dict(sorted(char_count.items()))
    print(sorted_char_count)

print(count_characters())