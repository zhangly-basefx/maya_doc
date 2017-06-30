# 返回maya版本号
cmds.about(v=True)

# 返回maya api版本
cmds.about(apiVersion=True)

# 返回maya运行时的编码
cmds.about(codeset=True)

# 返回用户是否存在网络链接
cmds.about(connected=True)

# 返回当前时间，格式为 Wed Jan 02 02:03:55 1980\n\0
cmds.about(ctime=True)


