def valid_palindrome(phrase: str) -> bool:
    # cleaned = ""
    cleaned = "".join(ch for ch in phrase.lower() if ch.isalnum())
    # second method. the up is shorter and cleaner
    # for p in phrase.lower():
    #     if p.isalnum():
    #         cleaned += p
    return cleaned == cleaned[::-1]


# approach 2
# two pointers


assert valid_palindrome("A man, a plan, a canal: Panama") is True, (
    "Different words gives True"
)
assert valid_palindrome("amanaplanacanalpanama") is True, (
    "same alphanumeric words on reverse gives True"
)
assert valid_palindrome("race a car") is False, "Classic sentence palindrome"
assert valid_palindrome(" ") is True, "empty string gives True"
