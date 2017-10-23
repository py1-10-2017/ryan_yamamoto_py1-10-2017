import random
def grades():
    for i in range(0, 10):
        random_num = random.randint(60, 101)
        if random_num >= 90:
            print "Score: ", random_num,"; Your grade is A"
        elif random_num >= 80:
            print "Score: ", random_num,"; Your grade is B"
        elif random_num >= 70:
            print "Score: ", random_num,";Your grade is C"
        elif random_num >= 60:
            print "Score: ", random_num,";Your grade is D"
        else:
            print "nothing"
    print "End of the program. Bye!"
grades()


# random.randint(a, b)
# Return a random integer N such that a <= N <= b.
