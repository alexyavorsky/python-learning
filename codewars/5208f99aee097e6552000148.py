def solution(s):
    new_s = ""
    for i in range(len(s)):
        if s[i] != s[i].upper():
            new_s += s[i]
        else:
            new_s += " " + s[i]
    return new_s
