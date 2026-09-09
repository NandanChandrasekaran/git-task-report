rows1=int(input("Enter number of rows for first matrix :"))
col1=int(input("Enter number of columns for first matrix :"))

rows2=int(input("Enter number of rows for second matrix :"))
col2=int(input("Enter number of columns for second matrix :"))

if col1!=rows2:
    print("Matrices cannot be multiplied")

MATRIX1=[]
MATRIX2=[]

for i in range(0,rows1):
    row=[]
    print("Enter elements of row",i+1,"of first matrix")
    for j in range(0,col1):
        row.append(int(input("Enter element: ")))
    MATRIX1.append(row)


for i in range(0,rows2):
    row=[]
    print("Enter elements of row :",i+1,"of second matrix")
    for j in range(0,col2):
        row.append(int(input("Enter element: ")))
    MATRIX2.append(row)

print("Matrix 1: ",MATRIX1)
print("Matrix 2: ",MATRIX2)

answer=[]

for i in range(0,rows1):
    result_row=[]
    for j in range(0,col2):
        sum=0
        for k in range(0,rows2):
            sum=sum+(MATRIX1[i][k]+MATRIX2[k][j])
        result_row.append(sum)
    answer.append(result_row)
print("Resultant matrix: \n")
for x in answer:
    print(x)
