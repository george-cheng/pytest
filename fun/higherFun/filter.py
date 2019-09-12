def not_empty(s):
    return s and s.strip()


f = list(filter(not_empty, ['a', '', 'c', '', 'aaa']))
print(f)
