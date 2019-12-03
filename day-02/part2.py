def run_instruction(instruction):
    for i in range(0, len(instruction), 4):
        if instruction[i] not in [1, 2, 99]:
            return -1
        elif instruction[i] == 99:
            break
        elif instruction[i] == 1:
            instruction[instruction[i+3]] = instruction[instruction[i+1]] + instruction[instruction[i+2]]
        elif instruction[i] == 2:
            instruction[instruction[i+3]] = instruction[instruction[i+1]] * instruction[instruction[i+2]]
    return instruction[0]


def main(input_):
    program = list(map(int, input_.strip().split(",")))
    for i in range(100):
        for j in range(100):
            instruction = program.copy()
            instruction[1], instruction[2] = i, j
            if run_instruction(instruction) == 19690720:
                return 100*i + j


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(main(input_))