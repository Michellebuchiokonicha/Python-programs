def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    anagram_s:dict[str, int] = {}
    anagram_t:dict[str, int] = {}
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



# method 2, using an helper function
def anagram_helper(text:str, helper_dict:dict[str, int]):
    for letter in text:
        if letter not in helper_dict:
            helper_dict[letter] = 1
        else:
            helper_dict[letter] += 1
    return helper_dict



def valid_anagram_with_helper(s:str, t:str) -> bool:
    if len(s) != len(t):
        return False

    anagram_dict_s = {}
    anagram_dict_t = {}
    anagram_first = anagram_helper(s, anagram_dict_s)
    anagram_second = anagram_helper(t, anagram_dict_t)
    return anagram_first == anagram_second


assert valid_anagram("anagram", "nagaram")==valid_anagram_with_helper("anagram", "nagaram") is True, "anagrams are rearranged"