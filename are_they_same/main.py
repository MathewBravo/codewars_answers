def comp(arr1, arr2):
    if arr1 is None or arr2 is None:
        return False
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if len(arr1) == 0 or len(arr2) == 0:
        return False
    arr2.sort()
    for i in arr1:
        if arr1.count(i) != arr2.count(i*i):
            return False
        if not binary_search(arr2, 0, len(arr2), i * i):
            return False
    return True


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return False


if __name__ == "__main__":
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    if comp(a1, a2):
        print("pass1")
    a1 = [121, 144, 19, 161, 19, 144, 19, 11]
    a2 = [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
    if not comp(a1, a2):
        print("pass2")
    a = [121, 144, 19, 161, 19, 144, 19, 11]
    b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
    if not comp(a1, a2):
        print("pass3")
