import math
import statistics


def list_mean(L):

    if L is None:
        return None

    if len(L) == 0:
        return None

    s = 0
    length = 0

    for l in L:
        if isinstance(l, float):
            s += l
            length += 1

        else:
            if isinstance(l, int):
                s += l
                length += 1
            else:
                print('Unsupported value in list.')
                continue

    return s/length


def list_stdev(L):
    if L is None:
        return None

    if len(L) == 0:
        return None

    nums = []

    for l in L:
        if isinstance(l, float):
            nums.append(l)
        else:
            if isinstance(l, int):
                nums.append(l)
            else:
                print('Unsupported value in list.')
                continue
    st = math.sqrt(sum([(statistics.mean(nums)-x)**2 for x in nums])/len(nums))
    return st
