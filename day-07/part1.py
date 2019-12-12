from itertools import permutations


class AmplifierController:
    def get_value(self, index, mode):
        if mode == "0":
            return self.program[self.program[index]]
        return self.program[index]

    def run_program(self, program, inputs):
        self.program = program
        inputs, output = iter(inputs), 0
        i = 0
        while i < len(program):
            opcode = str(self.program[i])[::-1] + '0' * (5 - len(str(self.program[i])))
            if int(opcode[:2][::-1]) == 99:
                break
            elif int(opcode[:2][::-1]) == 1:
                self.program[self.program[i+3]] = self.get_value(i+1, opcode[2]) + self.get_value(i+2, opcode[3])
                i += 4
            elif int(opcode[:2][::-1]) == 2:
                self.program[self.program[i+3]] = self.get_value(i+1, opcode[2]) * self.get_value(i+2, opcode[3])
                i += 4
            elif int(opcode[:2][::-1]) == 3:
                self.program[self.program[i+1]] = next(inputs)
                i += 2
            elif int(opcode[:2][::-1]) == 4:
                output = self.get_value(i+1, opcode[2])
                i += 2
            elif int(opcode[:2][::-1]) == 5:
                i = self.get_value(i+2, opcode[3]) if self.get_value(i+1, opcode[2]) != 0 else i + 3
            elif int(opcode[:2][::-1]) == 6:
                i = self.get_value(i+2, opcode[3]) if self.get_value(i+1, opcode[2]) == 0 else i + 3
            elif int(opcode[:2][::-1]) == 7:
                self.program[self.program[i+3]] = 1 if self.get_value(i+1, opcode[2]) < self.get_value(i+2, opcode[3]) else 0
                i += 4
            elif int(opcode[:2][::-1]) == 8:
                self.program[self.program[i+3]] = 1 if self.get_value(i+1, opcode[2]) == self.get_value(i+2, opcode[3]) else 0
                i += 4
            else:
                raise("Invalid opcode")

        return output

    def run_simulation(self, program, phase_settings):
        output = 0
        for x in phase_settings:
            output = self.run_program(program, inputs=[x, output])
        return output

    def main(self, program):
        program = list(map(int, program.strip().split(",")))
        phase_settings = permutations(range(5), 5)
        return self.run_simulation(program.copy(), list(phase_settings)[0])
        return max([self.run_simulation(program.copy(), phase_setting) for phase_setting in phase_settings])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(AmplifierController().main(program))
