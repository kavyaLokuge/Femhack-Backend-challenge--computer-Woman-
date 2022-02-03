
import math

##take inputs
##assuming all inputs are in SI units
launch_angle=float(input('Enter the launch angle(in degrees):'))
##convert angle to radians, since python takes radians as argument
launch_angle_radians=math.radians(launch_angle)
initial_velocity=float(input('Enter the initial velocity:'))
g=9.81#accleration due to gravity
#range (max horizontal distance), maximum height, time in the air of a projectile
max_horizontal_range=(initial_velocity**2)/g ##Rmax=(u*u)/g, occurs at 45degrees
horizontal_range=(initial_velocity**2)*math.sin(2*launch_angle_radians)/g##occurs at give angle
max_height=((initial_velocity**2)*(math.sin(launch_angle_radians)))/(2*g)# h=(usin(theta))^2 /2g
time_in_air=(2*initial_velocity*math.sin(launch_angle_radians))/g

print('Max Horizontal distance(Range)=',max_horizontal_range)#
print('Horizontal diatace=',horizontal_range)
print('Max height=',max_height)
print('Time in air=',time_in_air)

#You input the launch angle and the initial velocity of the projectile into the program
