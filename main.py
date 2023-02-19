# python3
# Linards Tomass Beķeris 221RDB161

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):

    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":

            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop()

            if not are_matching(top.char, next):
                return i + 1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"


def nolasit_failu(test_numb):

    faila_path = f"/workspaces/steks-un-iekavas-sprayzxd/test/{test_numb}"

    try:
        with open(faila_path, "r") as f:
            text = f.read().strip()
            return text
    except FileNotFoundError:
        print("invalid file path")
        return None


def process_input(input_type):

    if input_type.isdigit() and int(input_type) in range(6):
        text = nolasit_failu(input_type)
    elif input_type == "I":
        text = input("waiting for user to input the brackets: ")
    else:
        print("invalid input")
        text = None
    return text


def main():

    input_type = input().strip()
    text = process_input(input_type)

    if text:
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()
