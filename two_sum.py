def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums [j] == target:
                print(f"({i}, {j})")


if __name__ == "__main__":
    nums = []
    print("please enter the target :")
    target = int(input())
    print("enter the number of elements in the array")
    n = int(input())
    print("enter the elements")
    for i in range(n):
        nums.append(int(input()))
    two_sum(nums, target)
