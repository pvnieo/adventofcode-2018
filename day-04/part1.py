def respect_rules(number):
    number = str(number)
    if len(number) != 6:
        return False
    repeat = False
    for i in range(1, 6):
        if number[i] < number[i-1]:
            return False
        elif number[i] == number[i-1]:
            repeat = True

    return repeat


def main(input_):
    min_, max_ = map(int, input_.strip().split("-"))

    return sum([1 for x in range(min_, max_+1) if respect_rules(x)])


if __name__ == "__main__":
    input_ = "248345-746315"
    print(main(input_))
