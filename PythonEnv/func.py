def add(a, b, c):
    # print("a={},b={},c={}".format(a, b, c))
    # print(a + b + c)
    return a + b + c


# add(a=1, c=3, b=2)

# print(add(1, 2, 3))

# collection = ("hello", "world", 3)
# (a, b, c) = collection
#
# print(a)

def get_info(obj):
    return obj["name"], obj["age"]


(name, age) = get_info({"name": "小云", "age": 12})
print(name)
