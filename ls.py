'''
列出命令
'''

# 列出场景所有物体
cmds.ls()

# 列出选择的所有对象
cmds.ls(selection=True)

# 列出被选择多个对象中，最后一个被选择的元素
cmds.ls(selection=True, tail=True)

# 列出所有名为'sphere1'的对象，不会列出实例化的对象
cmds.ls('sphere1')

# 列出所有名为'sphere1'的对象，包含实例化对象
cmds.ls('sphere1', allPaths=True)

# 列出所有被选择的对象中，前缀为'group'的对象
cmds.ls('group*', selection=True)

# 列出所有的物体，灯光，摄像机
cmds.ls(geometry=True, lights=True, cameras=True)

# 列出所有的形状节点
cmds.ls(shapes=True)

# 列出所有几何形状节点，并显示它的类型
cmds.ls(type='geometryShape', showType=True)

# 列出所有变换对象
cmds.ls(transforms=True)

# 列出所有纹理贴图
cmds.ls(textures=True)

#列出所有references，排除未知的节点
cmds.ls(references=True)

#列出所有被锁定的节点(无法被删除更改)
cmds.ls(lockedNodes=True)
