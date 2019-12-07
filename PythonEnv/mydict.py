my_obj = {"name": "小云", "age": 10}
my_dict = dict(name="小云", age=12)

# print(my_obj)
# print(my_dict["age"])
# del my_obj["name"]

my_obj["name"] = "小明"

print(my_obj.get("name"))
