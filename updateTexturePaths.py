# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import os
import maya.cmds as cmds

# Arnold tiled texture extension
newExt = '.tx'

# List all textures in scene
textures = cmds.ls(type='file')

for text in textures:
    currentFile = cmds.getAttr("%s.fileTextureName" % text)
    ext = os.path.splitext(currentFile)[-1]
    if ext in ('.jpg', '.tiff', '.tif', '.tga'):
        newFile = currentFile.replace(ext, newExt)
        print "Updating %s \n\t --> %s" % (currentFile, newFile)
        cmds.setAttr("%s.fileTextureName" % text, newFile, type='string')
