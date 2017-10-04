words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
print words.replace("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]
print y[len(y)-1]
z = []
z.append(y[0])
z.append(y[len(y)-1])
print z

list = [19,2,54,-2,7,12,98,32,10,-3,6]
list.sort()
b = list[0:5]
c = list[5:len(list)]
print b
print c
c.insert(0, b)
print c
