import math

points=[(5,5),(2,1),(11,13),(2,1),(10,10)]
#a(x,y) b(x,y)



def euclidianDistance(a,b):

    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def distance(list):
    newList=[]
    i=0
    b=0
    while b<len(list)-1:
        i=0
        i+=b
        while i<len(list)-1:
            a=math.sqrt((list[b][0]-list[i+1][0])**2 + (list[b][1]-list[i+1][1])**2)
            newList.append(a)
            i+=1
        b+=1

    min=10000
    for i in newList:
        if i<min:
            min=i


    return newList,"The minimum distance of list is "+ str(min)


print(distance(points))








