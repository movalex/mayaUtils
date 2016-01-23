# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import os
import maya.cmds

textures = maya.cmds.ls(type='file')

for text in textures:
    currentFile = maya.cmds.getAttr(text+'.fileTextureName')
    ext = os.path.splitext(currentFile)[-1]
    if ext in ('.jpg', '.tiff', '.tif', '.tga'):
        maya.cmds.setAttr(text+".fileTextureName", currentFile.replace(ext, '.tx'), type='string')
        
