result_boolean = True
another_result_boolean = result_boolean
print(id(result_boolean))
print(id(another_result_boolean))

result_boolean = False
print(id(result_boolean))
print(id(another_result_boolean))

print("-" * 50)

result_string = "Audi"
another_result_string = result_string

print(id(result_string))
print(id(another_result_string))

result_string +=" great"
print(id(result_string))
print(id(another_result_string))