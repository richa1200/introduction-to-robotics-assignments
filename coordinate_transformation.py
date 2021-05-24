import numpy as np
import math

# coor = list(map(float , input('Enter coordinates of the point:').split(' ')))
# xt , yt, zt = [int(x) for x in input('Enter the translations for x,y,z:').split(' ')]
# theta_x = float(input('Enter rotation about x-axis:')) * math.pi / 180
# theta_y = float(input('Enter rotation about y-axis:')) * math.pi / 180
# theta_z = float(input('Enter rotation about z-axis:')) * math.pi / 180

xt , yt, zt = 0, 0, 0
theta_x = 30 * math.pi / 180
theta_y = 30 * math.pi / 180
theta_z = 30 * math.pi / 180
coor = [2,3,0]

rotation_x = [ [ 1,0,0],
[0 , math.cos(theta_x) , -math.sin(theta_x)],
[0 , math.sin(theta_x) , math.cos(theta_x)],]

rotation_y = [ [math.cos(theta_y) ,0,math.sin(theta_y)],
[0 , 1 , 0],
[-math.sin(theta_y) , 0 , math.cos(theta_y)],]

rotation_z = [ [ math.cos(theta_z), -math.sin(theta_z),0],
[math.sin(theta_z) , math.cos(theta_z) , 0],
[0 , 0 , 1],]

rotation_x = np.array(rotation_x)
rotation_y = np.array(rotation_y)
rotation_z = np.array(rotation_z)

rotation = ((rotation_x @ rotation_y) @ rotation_z)

transformation_matrix = [[rotation[0][0] , rotation[0][1],rotation[0][2],xt],
[rotation[1][0] , rotation[1][1],rotation[1][2],yt],
[rotation[2][0] , rotation[2][1],rotation[2][2],zt],
[0 ,0 ,0 ,1]]

coor.append(1.0)
coor = np.array(coor)

transformation_matrix = np.array(transformation_matrix)
sol = transformation_matrix @ coor
print('Solution Matrix:\n')
print(sol)