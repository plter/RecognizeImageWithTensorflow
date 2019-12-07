# for v in range(0, 100):
#     print(v)

count = 0

while count < 100:
    # if count % 2 == 0 and count % 3 == 0 and count % 4 == 0:
    #     print(count)
    if count % 3 == 0 or count % 4 == 0:
        print(count)
    count += 1
