# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import maya.cmds

selection = cmds.ls(sl=True)
cmds.select(all=True)
cmds.displaySmoothness(divisionsU=0, divisionsV=0, pointsWire=4, pointsShaded=1, polygonObject=1)
cmds.select(selection, r=True)
