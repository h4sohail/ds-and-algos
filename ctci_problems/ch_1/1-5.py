# Check if a string is one edit away from being correct
# Edit is, insert/remove/replace character
# So this means if we take two strings S1 and S2, S2 must have at least |S1| - 1 characters from S2
# pale, ple -> True because {p,l, e} = {p, a, l, e} \ a

def off_by_one(string1, string2):
    length1= len(string1)
    length2 = len(string2)
    error_cnt = 0
    if max(length1, length2) - min(length1, length2) > 1:
        return False

    for i in range(min(length1, length2)):
        if error_cnt > 1:
            return False
        if string1[i] != string2[i]:
            error_cnt += 1

    return True
print(off_by_one("test", "test12"))