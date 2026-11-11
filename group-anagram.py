# you are given a list of words, return the words grouped so that each group contains words that are anagrams of each other

# eg, Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def group_anagram(words: list[str]) -> list:
    groups: dict[str, list[str]] = {}
    for word in words:
        label = "".join(sorted(word))
        if label not in groups:
            groups[label] = [word]
        else:
            groups[label].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagram(words))
