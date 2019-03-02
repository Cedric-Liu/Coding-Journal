#Given a string, find the first non-repeating character in
# it and return it's index. If it doesn't exist, return -1.

def firstUniqChar(s: str) -> int:
    if not s:
        return -1
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    distinct = list(filter(lambda x: count[x] == 1, [key for key, value in
                                              zip(count.keys(),
                                                  count.values())]))
    if not distinct:
        return -1
    return min([s.find(item) for item in distinct])

firstUniqChar("leetcode")