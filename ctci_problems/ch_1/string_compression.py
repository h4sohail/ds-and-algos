# "aaa" -> "a3"
# "abca" -> "abca"


# check if current character is the same as the next character
# increment a count if it is else append character and count to response string and reset count

def compress_string(string):
    res = ''
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            res += string[i] + str(count)
            count = 1
    res += string[i] + str(count)
    if len(res) >= len(string):
        return string
    else:
        return res

