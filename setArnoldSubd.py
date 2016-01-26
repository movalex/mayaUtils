# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import maya.cmds as cmds

iterAttr = 'aiSubdivIterations'
typeAttr = 'aiSubdivType'
nIter = 2
typeVal = 1 # Catmull-Clark

# List all geo in scene
geoList = cmds.ls(geometry=True)

for geo in geoList:
    # Set number of iterations
    if cmds.attributeQuery(iterAttr, node=geo, ex=True):
        print "Setting %s.%s to %d" % (geo, iterAttr, nIter)
        cmds.setAttr("%s.%s" % (geo, iterAttr), nIter)
    # Set type of subdivision
    if cmds.attributeQuery(typeAttr, node=geo, ex=True):
        print "Setting %s.%s to %d" % (geo, typeAttr, typeVal)
        cmds.setAttr("%s.%s" % (geo, typeAttr), typeVal)
