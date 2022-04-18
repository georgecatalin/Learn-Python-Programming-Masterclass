odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

even.extend(odd)
print(even)

another_list = even
print(another_list)


print("-" * 50)
even.sort(reverse=False)
print(even)

even.sort(reverse=True)
print(even)

print(another_list)
