def max_sequence(arr) -> int:
    best_sum = 0
    current_sum = 0
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


if __name__ == '__main__':
    if max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6:
        print("Pass")
    else:
        print("returned value:" + str(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])))
    if max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155:
        print("Pass")
    else:
        print(
            "returned value:" + str(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43])))
