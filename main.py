"""Merge sort algorithm implementation."""

def merge(first_part: list[int], last_part: list[int]) -> list[int]:
    """
    Merges two sorted sublists into a single sorted list.

    This function takes two sorted lists, `first_part` and `last_part`, and combines
    them into a single sorted list in ascending order. It is typically used as part of
    the Merge Sort algorithm during the merge step.

    Parameters:
        first_part (list[int]): The first sorted sublist.
        last_part (list[int]): The second sorted sublist.

    Returns:
        list[int]: A new sorted list containing all elements from both input lists.
    """
    sorted_list = []
    i = j = 0

    while i < len(first_part) and j < len(last_part):
        if first_part[i] < last_part[j]:
            sorted_list.append(first_part[i])
            i += 1
        else:
            sorted_list.append(last_part[j])
            j += 1

    sorted_list.extend(first_part[i:])
    sorted_list.extend(last_part[j:])

    return sorted_list


def merge_sort(input_list: list[int]) -> list[int]:
    """
    Sorts a list of integers using the Merge Sort algorithm.

    This function implements the Merge Sort algorithm, a divide-and-conquer
    sorting technique. It recursively divides the input list into halves, sorts
    each half, and then merges them back together into a sorted list.

    Parameters:
        input_list (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: A new list containing the sorted elements of the input list.
    """
    if len(input_list) <= 1:
        return input_list

    division_index = len(input_list) // 2
    first_part = merge_sort(input_list[:division_index])
    last_part = merge_sort(input_list[division_index:])

    return merge(first_part, last_part)



if __name__ == "__main__":
    input_list = "Declare list here, example: [5, 4, 3, 2, 1]."
    input_list_sorted = merge_sort(input_list.copy())
    print(f"The list {input_list} sorted: {input_list_sorted}")
