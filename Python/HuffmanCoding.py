def frequency(string,char):
    char_count = 0
    for i in string:
        if i == char:
            char_count += 1

    return char_count

string = input("Please enter a string: ")
frequency_list = {}
for i in string:
    if i not in frequency_list:
        frequency_list[i] = frequency(string,i)

print(frequency_list)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
