'''
打开一个maya端口和外界的客户端进行链接
'''

# 打开默认名称为"mayaCommand"的端口
cmds.commandPort()

# 查询制定端口是否存在
cmds.commandPort('mayaCommand', q=True)

# 常用连接方式
if cmds.commandPort(":7010", q=True) != 1:
    cmds.commandPort(":7010", eo=False, nr=True)
