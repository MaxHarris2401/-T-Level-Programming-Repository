import math
Height = float(input("Enter the Height: "))
Radius = float(input("Enter the Radius: "))
Volume = math.pi*Radius*Radius*Height
SA = 2*math.pi*Radius*(Radius+Height)
print("Volume is",Volume)
print("Surface Area is ",SA)