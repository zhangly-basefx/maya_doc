'''
给物体添加删除父子关系
'''

# 将obj2指定为obj1的父级，不会被父级影响改变世界空间的位置
cmds.parent(obj1,obj2)

# 将obj2指定为obj1的父级，父级会对子级产生影响
cmds.parent(obj1,obj2,relative=True)

# 创建一个obj1的实例对象，保留obj1，成为obj2的子级
cmds.parent(obj1,obj2,add=True)

# 删除指定对象的父级
cmds.parent(obj, removeObject=True)

# 将obj1提出obj2，obj1会继承父级的属性信息
cmds.parent(obj,world=True)

# 从父级中删除形状节点
cmds.parent('nurbsSpahere3|nurbsSphereSpape1',shape=True,rm=True)

