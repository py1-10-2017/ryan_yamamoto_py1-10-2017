import random
def cointoss(count):
	coin = ""
	head = 0
	tail = 0
	for i in range(1, count):
		toss = random.randint(1, 2)
		if toss == 1:
			coin = "heads"
			head += 1
		else:
			coin = "tails"
			tail += 1
		print "Attempt #" + str(i) + ": " + "Throwing a coin...It's a " + coin + "!...Got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"


cointoss(5000)
