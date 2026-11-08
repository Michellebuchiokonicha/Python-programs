def anagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    s_count = {}
    t_count = {}
    for letter in s.upper():
        if letter not in s_count:
            s_count[letter] = 1
        else:
            s_count[letter] += 1

    for letter in t.upper():
        if letter not in t_count:
            t_count[letter] = 1
        else:
            t_count[letter] += 1

    return s_count == t_count


def count_letters(text: str) -> dict[str, int]:
    """Return how many times each character appears in text (case-sensitive)."""
    counts: dict[str, int] = {}
    for letter in text:
        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1
    return counts
            


def anagram_hel(s: str, t:str) -> bool:
    """Return True if t is an anagram of s, ignoring case."""
    if len(s) != len(t):
        return False
    return count_letters(s.lower()) == count_letters(t.lower())


assert count_letters("aab") == {"a": 2, "b": 1}, "count_letters: basic counts"
assert count_letters("") == {}, "count_letters: empty string has no counts"

for fn in (anagram, anagram_hel):
    assert fn("aab", "abb") is False, f"{fn.__name__}: Diff count gives False"
    assert fn("rat", "car") is False, f"{fn.__name__}: Different letters gives False"
    assert fn("", "") is True, f"{fn.__name__}: empty gives True"
    assert fn("a", "ab") is False, f"{fn.__name__}: different word length gives False"
    assert fn("anAgram", "nagaram") is True, f"{fn.__name__}: same letter count gives True"