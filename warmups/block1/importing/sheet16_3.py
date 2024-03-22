from trig_functions import tangent

base = float(input("How far are you from a tall structure? "))
theta = tangent(float(input("What is the angle of elevation from you to the top of the structure (in degrees)? ")))

print(theta*base)