# 배열을 입력받아 합으로 0을 만들 수 이쓴 3개의 엘리먼트를 출력하라.

nums = [-1, 0 , 1, 2, -1, -4]

# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

# 브루트 포스 계산
def code_complete_1(nums: list[int]):
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
