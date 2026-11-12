# valid palindrome


def valid_palindrome(pal: str) -> bool:
    # approach A
    cleaned = "".join(p for p in pal.lower() if p.isalnum())
    return cleaned == cleaned[::-1]

    # # approach longer than the first
    # cleaned = ""
    # for p in pal.lower():
    #     if p.isalnum():
    #         cleaned += p
    # return cleaned == cleaned[::-1]


# approach C
nums = [1, 2, 3, 4, 5, 6]
words = ["eat", "tea", "tan", "ate", "nat", "bat", "a"]
new_list = []
for num in nums:
    new_list.append(num * num)

new_list_a = [num * num for num in nums]

new_even = []
for num in nums:
    if num % 2 == 0:
        new_even.append(num)

new_even_a = [num for num in nums if num % 2 == 0]


new_odd = []
for num in nums:
    if num % 2 != 0:
        new_odd.append(num * num)

new_odd_a = [num * num for num in nums if num % 2 != 0]

distinct = set()
for word in words:
    distinct.add(len(word))

distinct_a = {len(word) for word in words}

new_dict = {}
for word in words:
    new_dict[word] = len(word)

new_dict_a = {word: len(word) for word in words}

old_string = "Hello, World! 123"
new_string = ""
for word in old_string.lower():
    if word.isalnum():
        new_string += word

clean_string = "".join(word for word in old_string.lower() if word.isalnum())


# sorting
sorted_dict = {}
for word in words:
    sorted_word = "".join(sorted(word))
    sorted_dict[word] = sorted_word
sorted_dict_a = {word: "".join(sorted(word)) for word in words}

assert valid_palindrome("A man, a plan, a canal: Panama" ) is True, "Classical palindrome"
assert valid_palindrome("race a car") is False, "not a palindrome"
assert valid_palindrome(" ") is True, "same when reversed, classical palindrome"
assert valid_palindrome("0P") is False, "not a palindrome"
assert valid_palindrome("a") is True, "same when reversed"
assert valid_palindrome("ab") is False, "not a palindrome"
assert new_list == new_list_a == [1, 4, 9, 16, 25, 36], "1: squares"
assert new_even == new_even_a == [2, 4, 6], "even nums"
assert new_odd == new_odd_a == [1, 9, 25], "odd numbers"
assert distinct == distinct_a == {1, 3}, "distinct, set"
assert new_dict == new_dict_a == {"eat": 3, "tea": 3, "tan": 3, "ate": 3, "nat": 3, "bat": 3, "a": 1}, "map, word length"
assert sorted_dict == sorted_dict_a == {"eat": 3, "tea": 3, "tan": 3, "ate": 3, "nat": 3, "bat": 3, "a": 1}, "map, word length"
assert new_string == clean_string == "helloworld123", "clean and old string"
assert sorted_dict == sorted_dict_a == {"eat": "aet", "tea": "aet", "tan": "ant", "ate": "aet", "nat": "ant", "bat": "abt", "a": "a"}, "clean and old string"




