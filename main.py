example = {"A": 0, "B": 3, "C": 5}


def length(target: dict[str, int]) -> int:
    span = max(target.values()) - min(target.values())
    return span


def get_first_character(target: dict[str, int]) -> str:
    minimum = min(target.values())

    for letter, index in target.items():
        if index == minimum:
            return letter


def main():
    print("Hello from nvidia-riddle!")

    text = "ADOBECODEBANC"
    target_letters = "ABC"
    target_length = len(target_letters)
    index = -1

    sub_string = dict()
    result = dict()
    for character in text:
        index += 1

        if character in target_letters:
            sub_string[character] = index

            if len(result) < target_length:
                result = sub_string.copy()
                continue
            if len(sub_string) == len(target_letters):
                if length(sub_string) <= length(result):
                    result = sub_string.copy()
                first_character = get_first_character(sub_string)
                del sub_string[first_character]

    result_string = text[min(result.values()) : max(result.values()) + 1]

    print(result_string)


if __name__ == "__main__":
    main()
