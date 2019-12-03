def restore_program_1202(input_):
    program = list(map(int, input_.strip().split(",")))
    program[1], program[2] = 12, 2
    for i in range(0, len(program), 4):
        if program[i] not in [1, 2, 99]:
            return -1
        elif program[i] == 99:
            break
        elif program[i] == 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        elif program[i] == 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
    return program[0]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read()
        print(restore_program_1202(input_))