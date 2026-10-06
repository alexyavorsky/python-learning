def solution(s):
    if len(s) % 2 == 0:
        f = [s[i:i+2] for i in range(0, len(s)-1, 2)]
    else:
        f = [s[i:i+2] for i in range(0, len(s)-1, 2)] + [f'{s[-1]}_']
    return(f)