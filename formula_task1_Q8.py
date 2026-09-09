"""Q8. Consider a CSV ( cones.csv ) with cone id, x, y, colour (blue or yellow) per row. Sort the rows by
distance from the origin. Write two new CSVs, one per colour, keeping the sorted order. Then find the
midpoint between every blue cone and its nearest yellow cone and write those midpoints to centreline.csv."""

import csv
import math

cones=[]
with open("cones.csv","r") as file:
    reader=csv.reader(file)
    header=True

    for row in reader:
        if header==True:
            header=False

        else:
            cone_id=row[0]
            colour=row[3]
            x=float(row[1])
            y=float(row[2])
            cone = {"id":cone_id,"x":x,"y":y,"colour":colour}
            cones.append(cone)

file.close()

def dist(cone):
    dist_origin=math.sqrt((cone["x"]**2) +(cone["y"]**2))
    return dist_origin

sortedcones=[]
for cone in cones: 
    distance=dist(cone)
    sortedcones.append((distance,cone))

sortedcones.sort()
cones=[]
for distance,cone in sortedcones:
    cones.append(cone)


bluecones=[]
yellowcones=[]
for cone in cones:
    if cone["colour"]=="blue":
        bluecones.append(cone)

    if cone["colour"]=="yellow":
        yellowcones.append(cone)

file= open("bluecones.csv","w",newline='')
writer=csv.writer(file)
writer.writerow(["id","x","y","colour"])
for cone in bluecones:
    writer.writerow([cone["id"],cone["x"],cone["y"],cone["colour"]])
file.close()


file= open("yellowcones.csv","w",newline='')
writer=csv.writer(file)
writer.writerow(["id","x","y","colour"])
for cone in yellowcones:
    writer.writerow([cone["id"],cone["x"],cone["y"],cone["colour"]])
file.close()

def distbwcones(cone_a,cone_b):
    dx=cone_a["x"]-cone_b["x"]
    dy=cone_a["y"]-cone_b["y"]
    dist=math.sqrt(dx**2+dy**2)
    return dist

midpoints=[]

for blue in bluecones:
    nearest=yellowcones[0]
    dist=distbwcones(blue,yellowcones[0])

    for yellow in yellowcones:
        d=distbwcones(blue,yellow)
        if d<dist:
            dist=d
            nearest=yellow

    mid_x=(blue["x"]+nearest["x"])/2
    mid_y=(blue["y"]+nearest["y"])/2

    midpoints.append({"x":mid_x,"y":mid_y})


file=open("centreline.csv","w",newline="")
writer=csv.writer(file)
writer.writerow(["x","y"])

for point in midpoints:
    writer.writerow([point["x"],point["y"]])
file.close()


        