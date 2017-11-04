from datetime import datetime

class Call(object):
    def __init__(self, uid, name, number, reason):
        self.uid = uid
        self.name = name
        self.number = number
        self.time = datetime.now()
        self.reason = reason
    def display(self):
        print "ID:{}".format(self.uid)
        print self.name
        print self.number
        print self.time.strftime('%c')
        print self.reason

class CallCenter(object):
    def __init__(self):
        self.call_list = []
        self.queue_size = 0
    def add(self, call):
        self.call_list.append(call)
        self.queue_size += 1
        return self
    def remove(self):
        self.call_list.pop(0)
        self.queue_size -= 1
        return self
    def remove_call(self, number):
		for x in self.call_list:
			if number == x.number:
				self.call_list.remove(x)
                self.queue_size -= 1
                return self
    def info(self):
        for call in self.call_list:
            print "Name: {} Phone Number: {}".format(call.name, call.number)
        print "Queue size: {}".format(self.queue_size)
cc = CallCenter()

caller2 = Call(2, "Mo", "808-123-4567", "sign up")
caller3 = Call(3, "BK", "408-098-7412", "cancel")
caller1 = Call(1, "RY", "123-456-7890", "complaint" )
cc.add(caller3).add(caller1).add(caller2).remove()
cc.info()
