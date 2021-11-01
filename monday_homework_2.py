n = input("Enter Pyramid Layers Here: ")

def pyramid(n):
    a = n - 1
    for c in range(0, n):
        for j in range(0, a):
            print(end=" ")
        a = a - 1
        for d in range(0, j+1):
            print("* ", end="")
        

#No idea if this would even work. My thought process is that since "n" is undefined, it needs to be an input. 
#So n needs to be subtracted by one for each layer. That's a simple calculation to determine the number of layers. 
#Then you need to calculate the width of each layer. So find the range between 0 and n (whatever was input). 
#This is where I'm not sure if I'm correct. Create an inner loop since you need something printed to form the pyramid. 
#You'll need to control spacing for various spacing, and I may have over complicated it. I figured find
#the distance from 0 to a and putting a space. I couldn't figure out how to \n and get a space, but I found on GeeksforGeeks about the end function.
#Then to shorten each layer as it looped, just make a=a-1 (a is the result of n-1, the input -1).
#To set the columns I needed to know the number of stars across, which requires knowing the range of 0 to n, with the value changing
#Then just print the result as stars. 