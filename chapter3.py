'''
Purpose: Teleports a player to different locations.
         Demonstrates usage of setTilePos and time.sleep
File Name: tour.py
Author: Khamani Williams
Dated: 6/12/2017
'''
import time 
from mcpi.minecraft import Minecraft

# Connect to Minecraft
mc = Minecraft.create()
#set co-ordinates x,y,z
original_x = 10
original_y = 0
original_z = -12
# Change the player's position (teleport)
mc.player.setTilePos(original_x, original_y, original_z)
time.sleep(3)

#teleport 125 times, every 200 milliseconds
for i in range (1,125):
    x = 5*i
    y = 110
    z = -12
    mc.player.setTilePos(x, y, z)
    time.sleep(0.2)
#end of for loop

#set player position back to original position
x = original_x
y = original_y
z = original_z
mc.player.setTilePos(x, y, z)
time.sleep(3)

#end of the program
