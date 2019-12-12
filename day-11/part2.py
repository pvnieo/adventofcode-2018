from collections import defaultdict


class PaintingRobot:
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

    def main(self, program):
        self.program = defaultdict(int)
        for i, x in enumerate(program.strip().split(",")):
            self.program[i] = int(x)

        self.relative_base = 0
        space_color = defaultdict(int)
        current_position = [0, 0]
        space_color[tuple(current_position)] = 1
        inputs, outputs, direction = [], [], "^"
        directions = ["^", "<", "v", ">"]
        next_direction = {(0, directions[i]): directions[(i+1) % 4] for i in range(4)}
        next_direction.update({(1, directions[i]): directions[(i-1) % 4] for i in range(4)})
        i = 0

        while i < len(program):
            opcode = str(self.program[i])[::-1] + '0' * (5 - len(str(self.program[i])))
            inputs = iter([space_color[tuple(current_position)]])
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
                break

            if len(outputs) == 2:
                space_color[tuple(current_position)] = outputs.pop(0)
                direction = next_direction[(outputs.pop(0), direction)]
                if direction == "^":
                    current_position[1] += 1
                elif direction == "v":
                    current_position[1] -= 1
                elif direction == ">":
                    current_position[0] += 1
                elif direction == "<":
                    current_position[0] -= 1

        xm, ym = min(space_color.keys(), key=lambda x: x[0])[0], min(space_color.keys(), key=lambda x: x[1])[1]
        xM, yM = max(space_color.keys(), key=lambda x: x[0])[0], max(space_color.keys(), key=lambda x: x[1])[1]
        registration_identifier = [[" " for i in range(xm, xM+1)] for j in range(ym, yM+1)]
        for x, c in space_color.items():
            if c:
                registration_identifier[x[1] - ym][x[0] - xm] = '#'

        return "\n".join(["".join(x) for x in registration_identifier][::-1])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(PaintingRobot().main(program))
