# "ABCDEF" -> true
# "ABCAEFX" -> false
# "" -> true
# "A" -> true


# Use a set
# set(string)
# check len
# compare to len(string)


# "ABC" = 3
# "ABC" = 3

# "AAB" = 3
# "AB" = 2


def has_duplicate(string):
    string = string.strip(' ') # Remove trailing whitespace on both sides
    string = string.strip('\n') # Remove trailing newline characters on both sides
    if string == "" or len(string) == 1:
        return True
    orignal_length = len(string)
    set_length = len(set(string))
    return set_length == orignal_length

print(has_duplicate(""))