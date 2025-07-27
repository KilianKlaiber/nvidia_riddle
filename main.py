example = {"A": 0, "B": 3, "C": 5}


def length(target: dict[str, int]) -> int:
    """Calculate the difference between the largest and smallest integer value """
    span = max(target.values()) - min(target.values())
    return span


def get_first_character(target: dict[str, int]) -> str:
    """Find the string with the smallest integer in the dictionary"""
    return min(target.keys(), key=lambda k: target[k])


def find_shortest_substring(text: str, target_letters: str) -> str:
    """
    Find the shortest substring that contains all target letters at least once.
    
    Args:
        text: The input string to search within
        target_letters: String containing all letters that must appear in the result
        
    Returns:
        The shortest substring containing all target letters
        
    Raises:
        ValueError: If no valid substring is found
    """
    target_length = len(target_letters)
    
    if not text or not target_letters:
        raise ValueError("Both text and target_letters must be non-empty")
    
    sub_string: dict[str, int] = {}
    result: dict[str, int] = {}
    for index, character in enumerate(text):

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

    if len(result) < target_length:
        raise ValueError(f"No substring found containing all letters: {target_letters}")
        
    result_string = text[min(result.values()) : max(result.values()) + 1]

    return result_string
    

def main():
    print("Hello from nvidia-riddle!")

    text = "ADOBECODEBANC"
    target_letters = "ABC"
    sub_string = find_shortest_substring(text, target_letters)
    
    print(sub_string)


if __name__ == "__main__":
    main()
