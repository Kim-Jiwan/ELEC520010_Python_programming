t1 = ('a', 'b', 'c')
t2 = 'a', 'b', 'c'

print(t1 + t2)

my_list = [ x for x in t1 ]
print(my_list)

my_list_duple = [ x + y for x in t1 for y in t2 ]
my_dict = { x : y for x in t1 for y in t2 }
print(my_dict)