splitString = "This string\nsplits\nover\nseveral lines"
tabbedString = "+40\t764\t836"

print(splitString)
print(tabbedString)

# using escape characters to escape special characters
print("I said 'go home'")
print('I said \'go home \'')
print(""" I said 'go home' """)

splitString_version_2 = """ This string
splits
over
several lines"""
print(splitString_version_2)


split_string_escape_end_of_Line = """This string \
splits \
over \
several \
lines """

print(split_string_escape_end_of_Line)