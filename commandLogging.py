'''
记录maya运行命令的日志
'''

# 设置命令日志记录的条目数
cmds.commandLogging(historySize=20)

# 查询命令日志记录的条目数
cmds.commandLogging(q=True, historySize=Ture)

# 查询命令日志的本地路径
cmds.commandLogging(q=True, logFile=True)

# 修改命令日志的路径
cmds.commandLogging(logFile='C:/temp/log.txt')

# 还原日志文件为默认
cmds.commandLogging(resetLogFile=True)

