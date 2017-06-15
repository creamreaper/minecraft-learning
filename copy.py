from mcpi.minecraft import Minecraft
mc = Minecraft.create()
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
(x,y,z)
print(position)
x = 80 + 5
y = 70 
z = -12
mc.player.setTilePos(x, y, z)
