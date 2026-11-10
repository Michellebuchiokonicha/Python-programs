def group_anagram(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in groups:
            groups[sorted_word] = [word]
        else:
            groups[sorted_word].append(word)
    return list(groups.values())


assert group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"],
], "Correct"
