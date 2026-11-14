nums = [1, 2, 3, 4, 5, 6]
words = ["eat", "tea", "tan", "ate", "nat", "bat", "a"]

plus_10 = []
for n in nums:
    plus_10.append(n + 10)

plus_10_a = [n + 10 for n in nums]

assert plus_10 == plus_10_a == [11, 12, 13, 14, 15, 16], " example: plus ten"

square_nums = []
for n in nums:
    square_nums.append(n * n)
# print(square_nums)

square_nums_a = [n * n for n in nums]
assert square_nums == square_nums_a == [1, 4, 9, 16, 25, 36], " example: square"
# odd squares
new_squares = []
for n in nums:
    if n % 2 != 0:
        new_squares.append(n * n)
    # print(new_squares)

new_squares_a = [n * n for n in nums if n % 2 != 0]
assert new_squares == new_squares_a == [1, 9, 25], " example: square"

# set
distinct = set()
for n in words:
    if len(n) not in distinct:
        distinct.add(len(n))
print(distinct)

distinct_a = {len(n) for n in words}


# dict
new_dict = {}
for word in words:
    if word not in new_dict:
        new_dict[word] = len(word)
print(new_dict)

new_dict_a = {}
new_dict_a = {word: len(word) for word in words}

assert (
    new_dict
    == new_dict_a
    == {"eat": 3, "tea": 3, "tan": 3, "ate": 3, "nat": 3, "bat": 3, "a": 1}
), " example: square"

string_pal = "Hello, World! 123"
cleaned = "".join(word for word in string_pal.lower() if word.isalnum())
assert cleaned == "helloworld123", "string: keep lowercase alphanumerics"


# 7. dict
labels = {word: "".join(sorted(word)) for word in words}
assert labels["eat"] == labels["tea"] == "aet", "dict: anagram labels"
