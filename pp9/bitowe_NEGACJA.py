print(~1)
# 00000001 (to jest 1 w systemie bitowym) => 11111110 (-2)

# 00000001 (1)
# 00000000 (0)
# 11111111 (-1)
# 11111110 (-2)


for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i, i))
print("*" * 20)

for i in range(5, -6, -1):
    print("{0:08b} => {1:d}".format(i & 255, i))