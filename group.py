'''
对组的操作命令
'''

# 创建一个空组
cmds.group(em=True, name='null1')

# 将指定对象放入新建的组
cmds.group('cube1','sphere1',name='group1')

# 创建一个新组，并设定它的父级
cmds.group(parent='null1', name='group2')

