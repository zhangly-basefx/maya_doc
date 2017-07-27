'''
解除组的命令（删除组，保留组内的所有对象）
'''

# 解除组，组内对象将会继承被删除的组的信息
cmds.ungroup('group1')

# 解除组，子物体将不继承组的信息
cmds.ungroup('group1', relative=True)

# 解除组，并将其子物体放入其它组
cmds.ungroup('group1', parent='group2')

# 解除组，将其子物体放入到最外层
cmds.ungroup('group1', world=True)

