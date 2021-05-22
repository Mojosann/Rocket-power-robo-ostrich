#-*-coding:UTF-8 -*-
# 智商很高的將不同shape rename

from maya import cmds

# 創造帶有shape_name的字典
SUFFIXES = {'mesh': 'geo', 'joint': 'jnt', 'camera': None, 'ambientLight': 'lgt'}

# 創造預設值
DEFAULT_SUFFIX = 'grp'


def rename(selection=False):

	'''
	This function will rename any object to have the correct suffix.

	Args:
		selection: whether or not we use the surrent selection
	Returns:
		A list of all the objects we operated on
	'''


	objects = cmds.ls(selection=True, dag=True, long=True)

	# This function connot run if there is no selection and no objects
	# 例外處理 如果selection為True, 但並沒有選擇任何obj就會出現錯誤

	if selection and not objects:

		# raise像是提出投訴: raise a complaint
		# 這裡的xxError可以查看python doc了解
		raise RuntimeError('You dont have anything selected, How dare you?')

	# 因為objects是list, 有sort這個method
	# key: 由短到長排列     加reverse可以改由長到短排列
	objects.sort(key=len, reverse=True)


	# 隨便選取一個東西然後印出來
	# 如果甚麼都不選 比較印出結果
	#print objects


	# 取值
	for obj in objects:

		shortName = obj.split('|')[-1]
		#print cmds.objectType(obj)

		# 印出objectType時候會出現transform是因為你可以在outliner右鍵按下shape,
		# 而shape確實是一個transform
		
		# 會印出shape name, 因為每一個obj都有shape的子層級(underworld)
		# 但也有可能為空值None(比如物件是一個empty grp), 於是在下方加個or []直接變成空清單
		children = cmds.listRelatives(obj, children=True, fullPath=True) or []
		#print children
		
		
		# 確保只有一個才能判斷物件型別
		# We will only do this if there is one child
		if len(children) == 1:
			child = children[0]
			objType = cmds.objectType(child)
		else:
			# Now we get the object type of the current object
			objType = cmds.objectType(obj) # 變成爸爸
			
		#print objType # mesh / transform / nurbsSurface...
		

		# 如果取不到objType, 預設值為DEFAULT_SUFFIX
		suffix = SUFFIXES.get(objType, DEFAULT_SUFFIX) 
		
		# camera = None, because None not belongs to True or False
		if not suffix:
			continue

		# if obj already rename, dont rename again
		# maybe帶有suffix的物件是要更名的所以要確定有_
		if obj.endswith('_' + suffix):
			
			# continue就可以跳過以下步驟
			continue

		# Now we need to construct the new name
		newName = '%s_%s' % (shortName, suffix)

		# Now tell it to rename the obj to the new name with the suffix
		cmds.rename(obj, newName)

		index = objects.index(obj)
		objects[index] = obj.replace(shortName, newName)

	# 程式執行結束 期望吐出一個object_list
	return objects