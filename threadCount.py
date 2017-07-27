'''
设置与查询maya在多线程代码区域中的线程数
'''

# 设置线程数为4
cmds.threadCount(n=4)

# 查询线程数
cmds.threadCount(q=True, n=True)

