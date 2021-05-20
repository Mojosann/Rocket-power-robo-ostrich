# 智商很高的將不同shape rename
from maya import cmds

def rename():
	
	selection = cmds.ls(selection=True)

	# dag = dag obj 意思是出現在outliner上的所有而且沒有被隱藏
	# long = full path of the object
	if len(selection) == 0:
		selection = cmds.ls(dag=True, long=True)

	# 因為selection是list, 有sort這個method
	# key: 由短到長排列     加reverse可以改由長到短排列
	selection.sort(key=len, reverse=True)


	# 隨便選取一個東西然後印出來
	# 如果甚麼都不選 比較印出結果
	print selection


	# 取值
	for obj in selection:
		shortName = obj.split('|')[-1]
		#print cmds.objectType(obj)

		# 印出objectType時候會出現transform是因為你可以在outliner右鍵按下shape,
		# 而shape確實是一個transform
		
		# 會印出shape name, 因為每一個obj都有shape的子層級(underworld)
		# 但也有可能為空值None(比如物件是一個empty grp), 於是在下方加個or []直接變成空清單
		children = cmds.listRelatives(obj, children=True, fullPath=True) or []
		print children
		
		
		# 確保只有一個才能判斷物件型別
		# We will only do this if there is one child
		if len(children) == 1:
			child = children[0]
			objType = cmds.objectType(child)
		else:
			# Now we get the object type of the current object
			objType = cmds.objectType(obj) # 變成爸爸
			
		print objType # mesh / transform / nurbsSurface...
		 
		 
		# suffix 後綴詞 
		# We use a bunch of if statements to find the suffix we want to add
		if objType == "mesh":
			suffix = 'geo'
			   	
		elif objType == "joint":
			suffix = 'jnt'

		elif objType == 'camera':
	   	
			# In the case of the camera, we will say to continue.
			# Continue means that we will continue on to the next item in the list and skip the rest of the logic for this one
			print "Skipping camera"
			continue
			     
		else:
			suffix = 'grp'

		# Now we need to construct the new name
		newName = shortName+"_"+suffix

		# Now tell it to rename the obj to the new name with the suffix
		cmds.rename(obj, newName)