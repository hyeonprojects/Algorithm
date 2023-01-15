import collections
import re


def most_common_word(paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split() if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(most_common_word(paragraph, banned))
