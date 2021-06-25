def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob[-1] == '?':  # will give you an error if the string is empty
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

# The key was the string method `isupper()`. It handles most edge cases perfectly.
# Link: <https://www.w3schools.com/python/ref_string_isupper.asp>
