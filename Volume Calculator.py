#Shayla Stausgaard
#250850256
#CS1026 Assignment 2

#create empty lists to store values in
cube = []
pyramid = []
ellipsoid = []

#function to calculate volume of a cube
def cubeVol(l):
    cubeVolume = (l ** 3)
    cubeVolume = round(cubeVolume, 2)
    print()
    print("The volume of a pyramid with a side length of {} is {}".format(l,cubeVolume))
    return cubeVolume
#function to calculate volume of a pyramid volume
def pyramidVol(b,h):
    pyramidVolume = (1/3) * (b ** 2) * h
    pyramidVolume = round(pyramidVolume, 2)
    print()
    print("The volume of a pyramid with a base of {} and height of {} is {}".format(b,h,pyramidVolume))
    return pyramidVolume

#function to calculate volume of a ellipsoid
def ellipsoidVol(x, y, z):
    import math
    ellipsoidVolume = (((((4/3) * math.pi) * x * y * z)))
    ellipsoidVolume = round(ellipsoidVolume, 2)
    print()
    print("The volume of a ellipsoid with radii of {}, {}, and {} is {}".format(x,y,z,ellipsoidVolume))
    return ellipsoidVolume

#function to store and prompt for user input
def shapeChoice():
    shapeChoice = input("Please enter what shape you would like to calculate the volume of:"
                        "cube, pyramid, ellipsoid, or quit ")
    shapeChoice = shapeChoice.upper()
    return shapeChoice()
def listPrint(thisList):
    for element in thisList :
        print(element, end=" ")

shapeChoice = ""

#while loop to call functions, and append the calculations to empty lists at the top
while shapeChoice != "QUIT":
    shapeChoice = input("Please enter what shape you would like to calculate the volume of:"
                        "cube, pyramid, ellipsoid, or quit ")
    shapeChoice = shapeChoice.upper()

    if shapeChoice == "CUBE":
        length = float(input("Please enter the side length of the square:"))
        resultC = cubeVol(length)
        cube.append(resultC)

    elif shapeChoice == "PYRAMID":
        base = float(input("Please enter the base of the pyramid"))
        height = float(input("Please enter the height of the pyramid"))
        resultP = pyramidVol(base, height)
        pyramid.append(resultP)


    elif shapeChoice == "ELLIPSOID":
        r1 = float(input("Please enter the value of the first radius"))
        r2 = float(input("Please enter the value of the second radius"))
        r3 = float(input("Please enter the value of the third radius"))
        resultE = ellipsoidVol(r1, r2, r3)
        ellipsoid.append(resultE)

#print results to the screen in a clear format
if len(cube) == 0 and len(pyramid) == 0 and len(ellipsoid) == 0:
    print("You have come to the end of the session. You did not perform any volume calculations.")

else:
    print()
    print("The volumes calculated for each shape are shown below")
    print("You calculated the volume(s) of {} cube(s):".format(len(cube)))
    listPrint(cube)
    print("")
    print("You calculated the volume(s) {} pyramid(s):".format(len(pyramid)))
    listPrint(pyramid)
    print("")
    print("You calculated {} ellipsoid(s):".format(len(ellipsoid)))
    listPrint(ellipsoid)


