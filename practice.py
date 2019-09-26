from time import sleep, gmtime, strftime, time, localtime, ctime

print(gmtime())
print(time())
print(ctime())
print(ctime(time()))
print(localtime())

# local = strftime("%Y-%m-%d %H:%M",  ctime(time()))
local = strftime("%Y-%m-%d %H:%M",  gmtime(time() + 10800))
print(local)





