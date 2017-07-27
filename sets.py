'''
查询，创建或更新集合成员的命令
'''

# 将选择的对象加入到集合
newSet1 = cmds.sets()

# 查询集合里的元素
cmds.sets(newSet1, q=True)

# 创建一个集合，将两个集合加入到新的集合中
cmds.sets(newSet1, newSet2, n='setOfSets')

# 创建集合只包含对象的顶点
cmds.sets('sphere1',n="ballVertices",v=1)

# 返回集合列表是否有公共成员
cmds.sets('ballVertices',ii=newSet1)

# 返回指定对象是否属于指定的集合
cmds.sets('sphere1',im=newSet1)

# 将对象从指定集合中删除
cmds.sets('sphere1',rm=newSet1)



