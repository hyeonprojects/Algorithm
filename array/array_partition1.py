

def array_pair_sum(nums: list[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum


def array_pair_sum2(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])


if __name__ == '__main__':
    data = [1, 4, 3, 2, 7]
    print(array_pair_sum(data))
    print(array_pair_sum2(data))