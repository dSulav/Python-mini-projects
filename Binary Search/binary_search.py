def binary_search(sequence, req_item):
    begin_index = 0
    end_index = len(sequence) - 1
    while (begin_index <= end_index):
        midpoint  = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == req_item:
            return midpoint
        elif req_item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1 
    return None

sequence_list = []
total_num  = int(input("Enter total number of items in a list : "))
for i in range(total_num):
    item = eval(input("Enter the item list[{}] : ".format(i)))
    sequence_list.append(item)
print(sequence_list)
req_item= eval(input("Enter the requred item to be searched : "))
    
print("Required item {} is found at index {}".format(req_item,binary_search(sequence_list,req_item)))