import collections

input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]


def group_anagrams(input: list[str]) -> list[list]:
    angrams = collections.defaultdict(list)

    for word in input:
        #정렬하여 딕셔너리에 추가
        angrams[''.join(sorted(word))].append(word)

    return list(angrams.values())


if __name__ == '__main__':
    print(group_anagrams(input_data))