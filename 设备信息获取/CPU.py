# cpu信息
#Linux系统cpu利用率有以下几个部分
#User Time，执行用户进程的时间百分比
#System Time，执行内核进程和中断的时间百分比
#Wait IO,由于IO等待使cpu处于idle（空闲）状态的时间百分比
#Idle，cpu处于空闲状态的时间百分比

import psutil
#获取cpu完成信息
def getCpuInfo():
    print(psutil.cpu_times())
#>>> scputimes(user=29.36, nice=0.0, system=26.59, idle=9619.35, iowait=64.78, irq=0.5, softirq=1.67, steal=0.0, guest=0.0)

def getObjectType():
    print(type(psutil.cpu_times()))
#>>> <class 'psutil._pslinux.scputimes'>
# user () 从系统启动开始累计到当前时刻，用户态的CPU时间，不包含 nice值为负进程。
# nice () 从系统启动开始累计到当前时刻，nice值为负的进程所占用的CPU时间
# system () 从系统启动开始累计到当前时刻，核心时间
# idle () 从系统启动开始累计到当前时刻，除IO等待时间以外其它等待时间
# iowait () 从系统启动开始累计到当前时刻，IO等待时间
# irq () 从系统启动开始累计到当前时刻，硬中断时间
# softirq () 从系统启动开始累计到当前时刻，软中断时间

# CPU使用率计算
#CPU在t1到t2时间段总的使用时间 = ( user2+ nice2+ system2+ idle2+ iowait2+ irq2+ softirq2) - ( user1+ nice1+ system1+ idle1+ iowait1+ irq1+ softirq1)
#CPU在t1到t2时间段空闲使用时间 = (idle2 - idle1)
#CPU在t1到t2时间段即时利用率 =  1 - CPU空闲使用时间 / CPU总的使用时间

#
def getCpuUzilization(interval):
    return psutil.cpu_percent(interval,percpu=False)

#interval：代表时间（秒），在这段时间内的cpu使用率
#percpu：选择总的使用率还是每个cpu的使用率。False为总体，True为单个，返回列表

#获取cpu逻辑个数
def getCpuLogicNum():
    return psutil.cpu_count()

# 计算方式：单个cpu核数*cpu个数*2（cpu cores 这个规格值，如果支持并开启ht）
# ht：intel的超线程技术(HT), 可以在逻辑上再分一倍数量的cpu core出来


#获取cpu物理个数
def getCpuNum():
    return psutil.cpu_count(logical=False)
# 计算方式：单个cpu核数*cpu个数
