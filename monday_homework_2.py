n = input("Enter Pyramid Layers Here: ")

def pyramid(n):
    layer = n - 1
    for rows in range(0, n):
        for value in range(0, layer):
            print(end=" ")
        layer = layer - 1
        for value in range(0, rows + 1):
            print("X ", end="")
        

#No idea if this works. 
#My thought was that 
# (1) there needs to be an input for n because it can't be infinity.
# (2) to visualize the pyramd think of it in layers and the number of layers needs an input
# (3) then you need to know the max number of rows across.
# (4) but you need to know the value of the row range (layers will be added up to the input) which can only be known by the input. 
# (5) now you need to reduce the number of layers for each loop
# (6) lastly, you need to have the number of columns adjust to the results of the outer loop (rows in range)
# (7) I figured out the logic part, and knew that printing "X" would be the easiest way to build. But I didn't know how to space the layers and rows
# (8) broke down and went to w3 and discovered the "end" function and its opperation within python. Useful tool. 
# (9) but for some reason it's not printing. I've exhausted my search on it