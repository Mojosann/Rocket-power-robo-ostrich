from maya import cmds

# 會選出所有的obj
print cmds.ls()

# 有選到的才會被印出來
cmds.ls(selection=True)


# maya裡面的判斷式運用

if statement is True:
	doSomething()

somethingElse()

或是

if statement is False:
	doSomething()

somethingElse()

# 在maya裡面空格與tab, 空格is better
# 不要混用

# 解釋一下shape：
# Shapes in Maya are selectable DAG objects that display in 3D views. 
# Meshes, NURBS surfaces and curves, and locators are just some examples of shapes. 
# Shapes are also dependency graph (DG) nodes that have attributes which can be connected to other nodes. 
# Shapes can be thought of as a container for geometry.