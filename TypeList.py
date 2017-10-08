list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def listtype(x):
    string = ""
    totalsum = 0

    for i in x:
        if isinstance(i, int) or isinstance(i, float):
            totalsum += i
        elif isinstance(i, str):
            string += i

    if string and totalsum:
        print "The list you entered is of mixed type"
        print "String:", string
        print "Sum: ", totalsum
    elif string:
        print "The list you entered is of string type"
        print "String: ", string
    else:
        print "The list your entered is of integer type"
        print "Sum: ", totalsum

listtype(list1)
listtype(list2)
listtype(list3)
