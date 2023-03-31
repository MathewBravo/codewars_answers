from typing import List


def containsDuplicate( nums: List[int]) -> bool:
    set_ver = set(nums)
    return not len(set_ver) == len(nums)

if __name__ == '__main__':
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate([1,2,3,4]))
