# a second advantage of the tuples is that they are immutable, can not be changed and they can be unpacked at all times

a = b = c = d = e = f = 11
print(a)

# unpacking a tuple
x, y, z = 11, 18, 43
print(x)
print(y)
print(z)

data = (10, 42, 55)
m, n, p = data
print(m)
print(n)
print(p)

# unpacking a list
my_list = [ 42, 23, 55]
# my_list.append(453) # will fetch an error
r, q , z = my_list
print(r)
print(q)
print(z)