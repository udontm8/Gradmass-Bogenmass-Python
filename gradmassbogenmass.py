#Gradmass zu Bogenmass
gradmass0=float(input("Gradmass in Grad(°): "))
from math import pi
bogenmass0=gradmass0*pi/180
print(f"Bogenmass: {round(bogenmass0, 5)}rad")

#Bogenmass zu Gradmass
bogenmass1=float(input("Bogenmass in Radiant(rad): "))
from math import pi
gradmass1=180*bogenmass1/pi
print(f"Gradmass: {round(gradmass1, 5)}°")