# Created by Pilar Molina Lopez
# https://github.com/pilarmolinalopez/mayaUtils
import maya.cmds as cmds

geoList = cmds.ls(geometry=True)

smoothAttrName = "aiSubdivIterations"
smoothValue = 2
typeAttrName = "aiSubdivType"
typeValue = 1

for geo in geoList:
    if cmds.attributeQuery(smoothAttrName, node=geo, ex=True):
        print "Setting %s.%s to %d" % (geo, smoothAttrName, smoothValue)
        cmds.setAttr("%s.%s" % (geo, smoothAttrName), smoothValue)
    if cmds.attributeQuery(typeAttrName, node=geo, ex=True):
        print "Setting %s.%s to %d" % (geo, typeAttrName, typeValue)
        cmds.setAttr("%s.%s" % (geo, typeAttrName), typeValue)
