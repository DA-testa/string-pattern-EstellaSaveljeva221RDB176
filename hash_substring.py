# Estella Saveljeva 221RDB176 7.grupa

def read_input():
     text = input()

    if "I" in text[:1]:
        text1 = input()
        text2 = input()
    else:
        with open("./tests/06", "r") as f:
            text1 = f.readline()
            text2 = f.readline()
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    result = []
    hash_pattern = hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        hash_text = hash(text[i:i + len(pattern)])
        if hash_text == hash_pattern:
            if text[i:i + len(pattern)] == pattern:
                result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

