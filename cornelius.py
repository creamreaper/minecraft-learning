'''
Purpose: Draws letter L and I inside minecraft
		 Flashes the letters for few seconds
         Demonstrates usage of  setPos, setBlock and time.sleep
File Name: cornelius.py
Author: Khamani Williams
Dated: 6/13/2017
'''

import time
from mcpi.minecraft import Minecraft

def clear_grid(mc, block_type, start_x, start_y, start_z, font_size):
    for i in range (1, 6*font_size):
        mc.setBlock(start_x + i, start_y, start_z, block_type )
        mc.setBlock(start_x - i, start_y, start_z, block_type )

def draw_I(mc, block_type, start_x, start_y, start_z, font_size):
    #draw the vertical leg of I
    for i in range (0, 12*font_size):
        mc.setBlock(start_x, start_y, start_z  + i, block_type )


def draw_L(mc, block_type, start_x, start_y, start_z, font_size):
    #draw the horizontal leg of L
    for i in range (0, 6*font_size):
        mc.setBlock(start_x - i, start_y, start_z, block_type )

    #draw the vertical leg of L
    for i in range (0, 12*font_size):
        mc.setBlock(start_x, start_y, start_z  + i, block_type )

def flash_letters(timeout):        
	#start co-ordinates
    x = 84
    y = 71
    z = -7
    space=-7 #space between letters
    melonblocktype = 103 #melon
    airblocktype = 0 #air

    #clean up previously drawn letters
    mc.player.setPos(x-1,y+20,z)
    clear_grid(mc, airblocktype, x,y,z, 1)
    draw_L(mc, airblocktype, x,y,z, 1)
    x = x + space
    draw_I(mc, airblocktype, x,y,z, 1)
    time.sleep(timeout)

    #draw L and I
    x = 84
    y = 71
    z = -7
    draw_L(mc, melonblocktype, x,y,z, 1)
    x = x + space
    draw_I(mc, melonblocktype, x,y,z, 1)
    time.sleep(timeout)



#main program starts here
   
# Connect to Minecraft
mc = Minecraft.create()
#flash letters in a loop
for i in range (1,20):
    flash_letters(0.2) 
