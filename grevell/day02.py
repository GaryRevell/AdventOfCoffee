#
# Day 2 Advent problem - http://adventofcode.com/2017/day/2
# Corruption checksum
#
def checksum(excel):
    return sum([max(i) - min(i) for i in excel])

if __name__ == '__main__':
    sheets = [[[5,1,9,5], [7,5,3] , [2,4,6,8]],
              [[1,2,3,4],  [9,5,1] , [10,20,30,-4]]]
    for s in sheets:
        csum = checksum(s)
        print(s,'=',csum)

