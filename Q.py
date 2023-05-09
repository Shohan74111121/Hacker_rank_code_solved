
import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


import math
import os
import random
import re
import sys


def pageCount(n, p):
    # Write your code here
    fornt = p//2
    if n % 2 == 0:
        back = (n-p+1)//2
    else:
        back = (n-p)//2
    return min(fornt, back)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
