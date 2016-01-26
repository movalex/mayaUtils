# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import maya.cmds as cmds

# Store current selection
selection = cmds.ls(sl=True)
# Select all
cmds.select(all=True)
# Set maya rough smoothness settings
cmds.displaySmoothness(divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1)
# Restore selection
cmds.select(selection, r=True)
