import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs="+")
    args = parser.parse_args()

    _index = 0
    _text = ""
    for _char in " ".join(args.text):
        # do not incriment the index number for a space
        if _char == " ":
            _text += " "
        else:
            _mod = _index % 2
            _index += 1
            _text += _char.upper() if _mod == 1 else _char.lower()
    print(_text)


if __name__ == "__main__":
    main()
