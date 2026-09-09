import math


def dist_sort():
    refx=int(input("Enter x coordinate of reference point:  "))
    refy=int(input("Enter y coordinate of reference point:  "))
    reference=(refx,refy)

    x=int(input("How many coordinates do you want to enter ?: "))
    coords=[]
    for i in range(x):
        x=int(input("Enter X Coordinate: "))
        y=int(input("Enter Y Coordinate : "))
        print("\n")

        coords.append((x,y))
    L=[]
    for pt in coords:
        dist=math.sqrt((pt[0]-reference[0])**2 + (pt[1]-reference[1])**2)
        L.append((dist,pt))

    L.sort()
    answer=[]
    for x in L:
        answer.append(x[1])

    return answer


t= dist_sort()
print(t)


