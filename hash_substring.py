# Estella Saveljeva 221RDB176 7.grupa

def read_input():
     print("[!] \tUse an input to choose files or input - F or I ?")
    textInput = input(":").upper()
    if "F" in textInput:
        print("[!] \tEnter file name or file path. For example '0'.")
         with open("./tests/06", "r") as f:
            text1 = f.readline()
            text2 = f.readline()
    elif "I" in textInput:
        print("[!] \tEnter text below.")
        text1 = input()
        text2 = input()
       
    else:
        print("[Err]:\tWrong input")
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
     
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

