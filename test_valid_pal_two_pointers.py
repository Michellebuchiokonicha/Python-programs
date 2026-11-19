from valid_pal_two_pointers import valid_palindrome

def test_classic_palindrome():
    assert valid_palindrome("A man, a plan, a canal: Panama") is True


def test_only_spaces_is_palindrome():
    assert valid_palindrome(" ") is True