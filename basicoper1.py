x = object
y = object

x_list = [x] * 10
y_list = [y] * 10
full_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("full_list contains %d objects" % len(full_list))

if x_list.count(x)==10 and y_list.count(y)==10:
    print("Almost there.....")

if full_list.count(x)==10 and full_list.count(y)==10:
    print("Great..!")