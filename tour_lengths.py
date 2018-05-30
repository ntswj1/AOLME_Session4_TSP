import math

def findHypotenuse(side1, side2):
    return math.sqrt(side1**2 + side2**2)
    
def findTourLength (Side1_list, Side2_list):
    total_distance = 0
    for i in range(len(Side1_list)):
        side1 = Side1_list[i]
        side2 = Side2_list[i]
        distance = findHypotenuse (side1, side2)
        total_distance = total_distance + distance
        print "i = " +str(i)
        print "side 1 = "+str(side1)
        print "side 2 = "+str(side2)
        print "distance = "+str(distance)
        print "total_distance = "+str(total_distance)
        print " "
    return total_distance
    
Side1_list = [2-0, 3-2] # Take the differences along the columns
Side2_list = [4-2, 5-2] # Take the differences along the rows
print "Tour length = " + str(findTourLength(Side1_list, Side2_list))