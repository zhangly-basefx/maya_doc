'''
类似于Freeze Transformations冻结属性归零
'''

# 默认false，如果为true则指定的属性将归零而不移动物体
cmds.makeIdentity(apply=True)

# 只冻结位移属性
cmds.makeIdentity(apply=True, translate=True)

# 只冻结旋转属性
cmds.makeIdentity(apply=True, rotate=True)

# 只冻结缩放属性
cmds.makeIdentity(apply=True, scale=True)

# 将所有数值归零
cmds.makeIdentity()

