def nested_sum(t):
    total = 0
    for sublist in t:
        total += sum(sublist)
    return total


def cumsum(t):
    cumulative = []
    total = 0
    for i in t:
        total += i
        cumulative.append(total)
    return cumulative


def middle(t):
    return t[1:-1]


def chop(t):
    del t[0]
    del t[-1]


def is_sorted(t):
    return all(t[i] <= t[i + 1] for i in range(len(t) - 1))


def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)


def has_duplicates(t):
    seen = set()
    for item in t:
        if item in seen:
            return True
        seen.add(item)
    return False


t = [[1, 2], [3], [4, 5, 6]]
print("Nested sum:", nested_sum(t))

t = [1, 2, 3]
print("Cumulative sum:", cumsum(t))

t = [1, 2, 3, 4]
print("Middle elements:", middle(t))

t = [1, 2, 3, 4]
chop(t)
print("List after chop:", t)

print("Is sorted:", is_sorted([1, 2, 2]))
print("Is sorted:", is_sorted(['b', 'a']))

print("Is anagram:", is_anagram('listen', 'silent'))
print("Is anagram:", is_anagram('hello', 'world'))

print("Has duplicates:", has_duplicates([1, 2, 3, 4, 5]))
print("Has duplicates:", has_duplicates([1, 2, 3, 4, 4]))
