'''
用于复制的命令
'''

# 复制的时候制定复制物体的名字
cmds.duplicate(name='someName')

# 只复制选择的节点，不会连子物体一起复制
cmds.duplicate(parentOnly=True)

# 重命名其子物体的名字，使其成为唯一
cmds.duplicate(renameChildren=True)

# 使用此标志，在返回值上，只会返回根节点
cmds.duplicate(returnRootOnly=True)

# 复制时将执行上一次的变换操作
cmds.duplicate(smartTransform=True)

