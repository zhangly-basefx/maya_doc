'''
给对象更名
'''

# 将名字a改为b
cmds.rename('a','b')

# 更名时不影响形状节点
cmds.rename('a','b',ignoreShape=True)
