# def groupAnagrams(strs):
#     def is_anagram(a, b):
#         count = {}
#         for char in a:
#             count[char] = count.get(char, 0) + 1
#         for char in b:
#             if not char in count.keys():
#                 return False
#             else:
#                 count[char] -= 1
#                 if count[char] < 0:
#                     return False
#         return sum(count.values()) == 0
#
#     hashdic = {}
#     used_index = []
#     for s1 in strs:
#         for s2 in strs:
#             if is_anagram(s1, s2) and strs.index(s2) not in used_index:
#                 hashdic[s1] = hashdic.get(s1, [])
#                 hashdic[s1].append(s2)
#                 used_index.append(strs.index(s2))
#     res = [hashdic[key] for key in hashdic.keys()]
#     return res

def groupAnagrams(strs):
    hashdic = {}
    for s in strs:
        if ''.join(sorted(s)) in hashdic.keys():
            hashdic[''.join(sorted(s))].append(s)
        else:
            hashdic[''.join(sorted(s))] = [s]
    return list(hashdic.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))