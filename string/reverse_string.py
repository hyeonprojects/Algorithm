
def reverse_string(input: list[str]) -> list[str]:
    left, right = 0, len(input) - 1

    while left < right:
        input[left], input[right] = input[right], input[left]
        left += 1
        right -= 1

    return input


def reverse_string2(input: list[str]) -> list[str]:
    input.reverse()
    return input


if __name__ == '__main__':
    input_data = ["h", "e", "l", "l", "e"]
    input_data2 = ["H", "a", "n", "n", "a", "h"]

    print(reverse_string(input_data))
    print(reverse_string(input_data2))

    print(reverse_string2(input_data))
    print(reverse_string2(input_data2))


