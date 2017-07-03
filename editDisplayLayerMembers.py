'''
用于查询和编辑显示层内的物体
'''

# 查询显示层的物体
cmds.editDisplayLayerMembers('displayLayer1',query=True)

# 将指定物体加入显示层
cmds.editDisplayLayerMembers('displayLayer1', 'sphere1', 'cone1')

# 此关键字为True，则只是将选择的对象加入显示层，忽略其子对象
cmds.editDisplayLayerMembers(noRecurse=True)

# 此关键字为True，则会返回对象的完整路径，否则只返回对象的名字
cmds.editDisplayLayerMembers(fullName=True)

