from mcpi.minecraft import Minecraft
mc = Minecraft.create()
position = mc.player.getTilePos()
x = position.x
y = position.y
z = position.z
(x,y,z)
print(position)
x = 85
y = 70 + 5
z = -12
mc.player.setTilePos(x, y, z)
