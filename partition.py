'''
用于查询添加或删除集合set到分区partition
'''

# 创建一个分区，将set1和set2存放到分区p1中
cmds.partition('set1','set2',n='p1')

# 创建一个空的分区可以包含渲染集
cmds.partition(render=True)

# 添加或删除集到分区
cmds.partition('set1',add='p1')
cmds.partition('set2',rm='p1')

# 查询分区里的所有集合
cmds.partition('p1',q=True)

# 查询分区是否是一个可包含渲染集的分区
cmds.partition('p1',q=True,render=True)

