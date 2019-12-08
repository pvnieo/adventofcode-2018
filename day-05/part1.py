class IntcodeComputer:
    def get_value(self, index, mode):
        if mode == "0":
            return self.program[self.program[index]]
        return self.program[index]

    def main(self, program, inputs=[1]):
        self.program = list(map(int, program.strip().split(",")))
        inputs, outputs = iter(inputs), []
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
                outputs.append(self.get_value(i+1, opcode[2]))
                i += 2
        return outputs


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(IntcodeComputer().main(program))
