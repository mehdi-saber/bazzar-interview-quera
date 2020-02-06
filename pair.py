n, k = map(int, input().split())
s1 = set(map(int, input().split()))
found = False
for el in s1:
    prim = k - int(el)
    if s1.__contains__(k - el):
        print('Yes')
        print(str(el) + ' ' + str(k - el))
        found = True
        break
if not found:
    print('No')