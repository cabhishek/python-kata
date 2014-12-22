"""
You are given N sticks, where each stick is of positive integral length. A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

Suppose we have 6 sticks of length

5 4 4 2 2 8
then in one cut operation we make a cut of length 2 from each of the 6 sticks. For next cut operation 4 sticks are left (of non-zero length), whose length are

3 2 2 6
Above step is repeated till no sticks are left.
"""

def cut_sticks(sticks):

    while sticks:
        print "Sticks to cut ->", len(sticks)

        cut_size = min(sticks)

        sticks = filter(lambda x:x,
                        map(lambda x: x-cut_size, sticks))


cut_sticks([1,2,3,4,3,3,2,1])
