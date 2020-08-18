# palindrome: character sequence on either ends of the mid point are relections, 
# eg "tac" -> "tac" and "cat" in "tacocat" where "o" is the mid point
#    "noon" -> "no" and "on" in "noon" where "" is the mid point                                                                               

# Observation for even
# "noon"
# len = 4
# "{n: 2, o: 2}" all values are 2

# Observation for odd
# "tacocat"
# len = 7
# #{t: 2, a: 2, c:2, o:1} only one value is 1, rest are 2

# odd length strings
# (length - 1)/2 characters need to appear exactly twice

# even length strings
# length/2 characters need to appear exactly twice

def count_twice(string):
    hash_map = {}
    count = 0
    for char in string:
        if char not in hash_map:
            hash_map[char] = 1
        else:
            hash_map[char] += 1
    for val in hash_map.values():
        if val == 2:
            count += 1
    return count

print(count_twice("tacocat"))
def is_palindrome_permutation(string):
    if string == "":
        return
    
    count = count_twice(string)
    length = len(string)

    if length % 2 == 0:
        return length / 2 == count
    else:
        return (length - 1) / 2 == count

print(is_palindrome_permutation("damam"))