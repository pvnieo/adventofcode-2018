from collections import defaultdict


class IntcodeComputer:
    def get_value(self, index, mode):
        if mode == "0":
            return self.program[self.program[index]]
        elif mode == '2':
            return self.program[self.relative_base + self.program[index]]
        return self.program[index]

    def get_index(self, index, mode):
        if mode == "0":
            return self.program[index]
        elif mode == '2':
            return self.relative_base + self.program[index]
        return index

    def main(self, program, inputs=[2]):
        self.program = defaultdict(int)
        for i, x in enumerate(program.strip().split(",")):
            self.program[i] = int(x)

        self.relative_base = 0
        inputs, outputs = iter(inputs), []
        i = 0

        while i < len(program):
            opcode = str(self.program[i])[::-1] + '0' * (5 - len(str(self.program[i])))
            if int(opcode[:2][::-1]) == 1:
                self.program[self.get_index(i+3, opcode[4])] = self.get_value(i+1, opcode[2]) + self.get_value(i+2, opcode[3])
                i += 4
            elif int(opcode[:2][::-1]) == 2:
                self.program[self.get_index(i+3, opcode[4])] = self.get_value(i+1, opcode[2]) * self.get_value(i+2, opcode[3])
                i += 4
            elif int(opcode[:2][::-1]) == 3:
                self.program[self.get_index(i+1, opcode[2])] = next(inputs)
                i += 2
            elif int(opcode[:2][::-1]) == 4:
                outputs.append(self.get_value(i+1, opcode[2]))
                i += 2
            elif int(opcode[:2][::-1]) == 5:
                i = self.get_value(i+2, opcode[3]) if self.get_value(i+1, opcode[2]) != 0 else i + 3
            elif int(opcode[:2][::-1]) == 6:
                i = self.get_value(i+2, opcode[3]) if self.get_value(i+1, opcode[2]) == 0 else i + 3
            elif int(opcode[:2][::-1]) == 7:
                value = 1 if self.get_value(i+1, opcode[2]) < self.get_value(i+2, opcode[3]) else 0
                self.program[self.get_index(i+3, opcode[4])] = value
                i += 4
            elif int(opcode[:2][::-1]) == 8:
                value = 1 if self.get_value(i+1, opcode[2]) == self.get_value(i+2, opcode[3]) else 0
                self.program[self.get_index(i+3, opcode[4])] = value
                i += 4
            elif int(opcode[:2][::-1]) == 9:
                self.relative_base += self.get_value(i+1, opcode[2])
                i += 2
            else:
                assert int(opcode[:2][::-1]) == 99, "Opcode not found: {}".format(opcode)
                return outputs[0]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(IntcodeComputer().main(program))
