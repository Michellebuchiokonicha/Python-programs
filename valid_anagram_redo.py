def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    anagram_s: dict[str, int] = {}
    anagram_t: dict[str, int] = {}
    for letter in s.lower():
        if letter not in anagram_s:
            anagram_s[letter] = 1
        else:
            anagram_s[letter] += 1

    for letter in t.lower():
        if letter not in anagram_t:
            anagram_t[letter] = 1
        else:
            anagram_t[letter] += 1
    return anagram_s == anagram_t


# using a helper function


def count_letters(text: str) -> dict[str, int]:
    text_dict: dict[str, int] = {}
    for letter in text:
        if letter not in text_dict:
            text_dict[letter] = 1
        else:
            text_dict[letter] += 1
    return text_dict


def valid_anagram_with_helper(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    anagram_first = count_letters(s.lower())
    anagram_second = count_letters(t.lower())
    return anagram_first == anagram_second


assert (
    valid_anagram("anagram", "nagaram")
    is True
    == valid_anagram_with_helper("anagram", "nagaram")
    is True
), "anagrams are rearranged"
assert (
    valid_anagram("Listen", "Silent")
    is True
    == valid_anagram_with_helper("Listen", "Silent")
    is True
), "anagrams are rearranged"
assert valid_anagram("", "") is True == valid_anagram_with_helper("", "") is True, (
    "anagrams are rearranged"
)
assert (
    valid_anagram("a", "ab") is False == valid_anagram_with_helper("a", "ab") is False
), "not anagram"
assert (
    valid_anagram("aab", "abb")
    is False
    == valid_anagram_with_helper("aab", "abb")
    is False
), "not anagram"
assert (
    valid_anagram("rat", "car")
    is False
    == valid_anagram_with_helper("rat", "car")
    is False
), "not an anagram"


for fn in (valid_anagram, valid_anagram_with_helper):
    assert fn("anagram", "nagaram") is True, f"{fn.__name__}: basic anagram"
    assert fn("Listen", "Silent") is True, f"{fn.__name__}: should ignore case"
    assert fn("", "") is True, f"{fn.__name__}: two empty strings are anagrams"
    assert fn("a", "ab") is False, f"{fn.__name__}: different lengths"
    assert fn("aab", "abb") is False, f"{fn.__name__}: same letters, different counts"
    assert fn("rat", "car") is False, f"{fn.__name__}: different letters"
