import sys
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_converted=[i.split("=") for i in lst_in]
d = {}
for i in lst_converted:
    d[int(i[0])]=i[1]
print(*sorted(d.items()))
# print(lst_converted)