from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 80
y = 70
z =- 11
blockType = 103
up = 1
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + up, z, blockType)
