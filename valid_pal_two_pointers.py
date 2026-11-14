# I think 0 and the full length of the pal since its the end. minus 1
# so we need to check that if you reverse it, it will be thesame. I think you compare the last and the first
#  you compare the second to the last(-1,-2) and the second (1,2), then continue doing it.
# where to stop. if you get to the middle and you are able to compare, then its a palindrome, but if not able to compare and that is the last word, stop. it means its a palindrome
# if s[left] is not alnum, skip, continue, or even filter initially so the comparison is betweeon only alnum. we'd see
# I think left moves +1, right moves -1. since it will take it more into the string
# if it finishes without a mismatch, return True. but at anypoint you see mismatch, stop and return false.
# ab left = 0, right = 2-1=1 at index 0, it is a, at index 1, it is b so no match, == false
# aba at index 0, its a, at index 2, its a. good. then at index 1, it is b(middle), at index 1 for right, it is b(middle) so they match. True


def valid_palindrome(pal: str) -> bool:
    left = 0
    right = len(pal) - 1  # so that it is the exact indexes and not more
    while left < right:
        if not pal[left].isalnum():
            left += 1
            continue
        if not pal[right].isalnum():
            right -= 1
            continue
        if pal[left].lower() != pal[right].lower():
            return False
        left += 1
        right -= 1
    return True


assert valid_palindrome("A man, a plan, a canal: Panama") is True, (
    "classic: ignores case, spaces, punctuation"
)
assert valid_palindrome("race a car") is False, "mismatch in the middle -> False"
assert valid_palindrome(" ") is True, (
    "only non-alnum chars -> empty after cleaning -> True"
)
assert valid_palindrome("0P") is False, "digits count as alnum; '0' != 'p'"
assert valid_palindrome("a") is True, "single char is always a palindrome"
assert valid_palindrome("ab") is False, "two different chars -> False"
