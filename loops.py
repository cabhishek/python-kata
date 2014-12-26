def loop(intervals):

    print 'Basic'
    for interval in intervals:
        print interval

    print 'Basic + Loop index'
    for i, interval in enumerate(intervals):
        print i, interval

    print 'Start from index 1'
    for i in range(1, len(intervals)):
        print intervals[i]

    print 'Choose index and start position'
    for i, interval in enumerate(intervals[1:], start=1):
        print i, interval

    print 'Basic while loop'
    i = 0
    while i < len(intervals):
        print i, intervals[i]
        i +=1

    print 'Simulate \'while\' with \'for\''
    for i in range(len(intervals)):
        print i, intervals[i]

    print 'Basic backward loop'
    for interval in intervals[::-1]:
        print interval

    print 'Loops with flexible step interval'
    for interval in intervals[::2]:
        print interval

    print 'Iterate Curr and next element'
    for (curr, next) in zip(intervals, intervals[1:]):
        print curr, next

loop([[1,3],[2,6],[8,10],[9,18],[19,23]])
