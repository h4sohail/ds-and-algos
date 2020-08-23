# "ABC"
# "CBA"
# -> true

# "ABC"
# "BCAD"
# -> false

# "ABCC"
# "ABC"
# -> false

# ""
# ""
# -> true

# ""
# " "
# -> false

# check if length is the same, if not return false

def is_permute(str1, str2):
    if len(str1) != len(str2):
        return False
    
    return set(str1) == set(str2)
