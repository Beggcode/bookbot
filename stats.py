def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    result = {}
    for char in text:
        char = char.lower()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_char_count(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha(): #skips symbols, punctuation, spaces, etc.
            sorted_list.append({"char": char, "num": count})

    # sort by "num" in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
