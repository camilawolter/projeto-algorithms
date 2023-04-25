
def combine(left_half, right_half):
    i = j = 0
    result = []

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left_half = merge_sort(array[:middle])
    right_half = merge_sort(array[middle:])

    return combine(left_half, right_half)


def is_anagram(first_string, second_string):
    first_string = first_string.lower().replace(" ", "")
    second_string = second_string.lower().replace(" ", "")

    if first_string == "" and second_string == "":
        return ("", "", False)

    sorted_first_string = merge_sort(list(first_string))
    sorted_second_string = merge_sort(list(second_string))

    result = ("".join(sorted_first_string), "".join(
        sorted_second_string), sorted_first_string == sorted_second_string)

    return result
