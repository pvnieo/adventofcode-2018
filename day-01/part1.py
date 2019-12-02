def compute_mass(input_):
    return sum([max(int(n) // 3 - 2, 0) for n in input_.strip().split('\n')])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(compute_mass(input_))