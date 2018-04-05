#
# Advent problem from day one - http://adventofcode.com/2017/day/1
#
def captcha(myStr):
    return sum([int(myStr[c]) for c in range(-1,len(myStr)-1) if myStr[c]==myStr[c+1]])

myStrs = {'1122':3,'1111':4,'1234':0,'91212129':9}

if __name__ == '__main__':
    for m in myStrs:
        print(m,captcha(m)==myStrs[m])
