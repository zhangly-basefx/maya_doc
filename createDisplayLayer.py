'''
创建显示层
'''

# 只创建一个空的显示层
cmds.createDisplayLayer(empty=True)

# 创建显示层，并选择此显示层
cmds.createDisplayLayer(makeCurrent=True)

# 创建显示层并指定名字
cmds.createDisplayLayer(name='someName')

# 如果为True，则只将选择的物体加入选择层，忽略子物体
cmds.createDisplayLayer(noRecurse=True)

# 创建渲染层设置其层编号
cmds.createDisplayLayer(number=1)
