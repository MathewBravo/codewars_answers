def remove_smallest(numbers):
    
    if len(numbers) == 0:
        return numbers
    lowest = min(numbers)
    index = 0
    for i, val in enumerate(numbers):
        if val == lowest:
            index = i
            break
    return (numbers[:index] + numbers[index+1:])


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5]
    rest = remove_smallest(test)
    print(rest)
