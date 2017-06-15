'''
Purpose: Explains difference between variables, function, module, objects and their usage
File Name: Building.py
Author: Khamani Williams
Dated: 6/14/2017
'''
from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
width = 6
height = 6
length = 6
blockType = 4 #4 is cobblestone
air = 0
time.sleep(5)
r = mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType)
r = mc.setBlocks(x + 1, y +1 , z +1 , x + width -1, y + height -1, z + length - 1, air)
r = mc.setBlock(x + 3, y + 0, z, air)
r = mc.setBlock(x + 3, y + 1, z, air)
r = mc.setBlock(x + 3, y + 2, z, air)
print ("player position:", x,y,z)


'''
Variable can have values. They are on the left size of = operator
      example of variables in the above code:
             mc, pos, x,y,z, width, height, length, blocktype, r

function typically do some work. they contain () and may have zero or more arguments
      example of functions in above code
            create(), getPos(), setBlocks,print, sleep
      
module
      contains code that we can reuse later
       module file: mcpi.minecraft
       module name: Minecraft, time
             time is a built-in module
             minecraft is an imported module
object
      
    package two things. typically its on the left side of the . (dot)
          variables
          functions
          objects

      example  mc, mc.player,  pos
      
'''
