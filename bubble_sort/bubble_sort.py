def bubble_sort(unsorted_list):
    # Bubble sort implementation
    for i in range(len(unsorted_list) - 1, 0, -1):
        for j in range(i):
            if unsorted_list[j] > unsorted_list[j + 1]:
                # Swap elements
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

    print("Bubble sort is done")
unsorted_list= [5, 3, 8, 6, 7, 2]
bubble_sort(unsorted_list)
print(unsorted_list)  
