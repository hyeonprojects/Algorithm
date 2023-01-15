
def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum2(nums: list[int], target: int) -> list[int]:
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


def two_sum3(nums: list[int], target: int) -> list[int]:
    nums_maps = {}

    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_maps[num] = i

    # 타겟에서 첫 번쨰 수를 뺸 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_maps and i != nums_maps[target - num]:
            return [i, nums_maps[target - num]]


if __name__ == '__main__':
    nums, target = [2, 7, 11, 15], 9
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
