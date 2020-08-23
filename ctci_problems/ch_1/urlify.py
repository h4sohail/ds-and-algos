# "Mr John Smith    " clean the string
# "Mr John Smith" # replace spaces with %20
# "Mr%20John%20Smith"

# "" -> do nothing

def urlify(string):
    if string == "":
        return

    string = string.strip()
    return string.replace(' ', '%20')




