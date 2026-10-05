def find_outlier(integers):
    t1 = [i for i in integers if abs(i) % 2 != 0]
    t2 = [i for i in integers if abs(i) % 2 == 0]
    if len(t1) == 1:
        return t1[0]
    return t2[0]
