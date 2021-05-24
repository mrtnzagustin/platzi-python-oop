import random


def bubble_sort(my_list):
    # tipical bubble sort
    # n times: change the adjacent values to sort them
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list)-i-1):
            if my_list[j]>my_list[j+1]:
                aux = my_list[j+1]
                my_list[j+1] = my_list[j]
                my_list[j] = aux

def insert_sort(my_list):
    for i in range(0, len(my_list)):
        min_position = 0
        min_value = 2147483647
        # looks for the minimium value in the remain values
        for j in range(i, len(my_list)):
            if my_list[j] < min_value:
                min_position = j
                min_value = my_list[j]
        
        # change the current iteration position of the list to the min value and continues
        # with the rest of the list
        my_list[min_position] = my_list[i]
        my_list[i] = min_value

def merge_sort(my_list):
    if len(my_list) > 1:
        med = len(my_list) // 2
        left = my_list[:med]
        right = my_list[med:]
        
        # recursive call for each half
        merge_sort(left)
        merge_sort(right)

        # iterators to cycle through two sub lists
        i = 0
        j = 0
        # iterator to cycle through the list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k +=1

        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1

    return my_list

def run():
    list_size = int(input('List size: '))
    
    my_list = [random.randint(0,100) for i in range (list_size)]
    print(my_list)
    #bubble_sort(my_list)
    #insert_sort(my_list)
    merge_sort(my_list)
    print(my_list)


if __name__ == '__main__':
    run()