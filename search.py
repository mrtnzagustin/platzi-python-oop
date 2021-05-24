import random
import sys

def lineal_search(my_list, element):
    match = False

    for actual_element in my_list:
        if element == actual_element:
            match = True
            break
    
    return match

def binary_search(my_list, start, end, element):
    if start > end:
        return Flase
    
    med = (end - start) // 2

    if my_list[med] == element:
        return True
    elif my_list[med] > element:
        return binary_search(my_list, start, med - 1, element)
    else:
        return binary_search(my_list,med + 1 , end, element)
    

def run():
    try:
        print(f'The recursion limit is {sys.getrecursionlimit()}')
        
        list_size = int(input('List size: '))
        element_to_find = int(input('Element to find: '))
            
        my_list = [random.randint(0,100) for i in range (list_size)]
        match = lineal_search(my_list, element_to_find)
        
        print(my_list)
        print(f'The element {element_to_find} { "has been found" if match else "has not been found" }')

        my_list = sorted(my_list)
        match = binary_search(my_list, 0, len(my_list), element_to_find)

        print(f'The element {element_to_find} { "has been found" if match else "has not been found" }')

    except Exception as exception:
        print(f'Error: {exception.__str__()}')

if __name__ == '__main__':
    run()