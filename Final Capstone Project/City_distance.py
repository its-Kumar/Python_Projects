from math import *


def distance(coord1, coord2):
    """
        This uses the formula  'haversine' to calculate the great-circle distance b/w two points - that is the shortest distance over the earth surface.

    """

    lat1, long1 = coord1
    lat2, long2 = coord2
    R = 6371
    a = (sin((lat2 - lat1)/2))**2 + cos(lat1) * \
        cos(lat2)*(sin((long2 - long1)/2))**2
    c = 2 * (atan2(a**0.5, (1-a)**0.5))
    d = R * c
    return d


if __name__ == "__main__":
    print("\n\nEnter  The co-ordinate of two cities : \n")
    latitude1, longitude1 = (float(x) for x in input(
        "Enter Latitude and Longitude : ").split())
    latitude2, longitude2 = (float(x) for x in input(
        "Enter Latitude and Longitude : ").split())

    dist = distance((latitude1, longitude1), (latitude2, longitude2))

    print("Choose your unit to display : ")
    print("The Distance between two cities : \n")
    print("1. Kilometers\n2. Meters\n3. Miles\n4. Inches\n5. Foot\n6. Yard\n7. Light Year\n0. Exit")
    ch = int(input("Enter your choice : "))
    if ch == 0:
        print("Thank You..!!")
        exit()
    elif ch == 1:
        pass
    elif ch == 2:
        pass
    elif ch == 3:
        pass
    elif ch == 4:
        pass
    elif ch == 5:
        pass
    elif ch == 6:
        pass
    elif ch == 7:
        pass
    else:
        print("Wrong Choice..!!")
        print("Try Again....")
    print(dist)
