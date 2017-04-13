def validate(files):
    max = 0
    seen = {}
    for file in files:
        input = open(file, 'r')
        line = input.readline()
        while line:
            check = int(line)
            if check > max:
                max = check
            if check in seen:
                seen[check].append(file)
            else:
                seen[check] = [file]
            line = input.readline()
        input.close()
    flag = True
    for i in xrange(1, max + 1):
        if i not in seen:
            print str(i) + ' is missing'
            flag = False
        elif len(seen[i]) > 1:
            print str(i) + ' was downloaded in ' + str(seen[i])
            flag = False
    if flag:
        print 'All good'

def count(files):
    count = 0
    for file in files:
        input = open(file, 'r')
        line = input.readline()
        while line:
            count += 1
            line = input.readline()
        input.close()
    print count

def merge(inputs, output):
    out = open(output, 'a')
    for input in inputs:
        inp = open(input, 'r')
        line = inp.readline()
        while line:
            out.write(line)
            line = inp.readline()
        inp.close()
    out.close()

validate(['log1.log', 'log2.log', 'log3.log', 'log4.log', 'log5.log', 'log6.log', 'log7.log', 'log8.log'])
count(['recipes1.data', 'recipes2.data', 'recipes3.data', 'recipes4.data'])
count(['reviews1.data', 'reviews2.data', 'reviews3.data', 'reviews4.data'])
