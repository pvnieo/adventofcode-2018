import time
from collections import defaultdict


class CarePackage:
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

    def draw_game(self):
        xm, ym = max(self.screen.keys(), key=lambda p: p[0])[0], max(self.screen.keys(), key=lambda p: p[1])[1]
        screen = [[" " for _ in range(xm+1)] for _ in range(ym+2)]
        for k, v in self.screen.items():
            screen[k[1]][k[0]] = v
        print("\n".join(["".join(x) for x in screen]) + "\r", end="")

    def main(self, program, cheat=True):
        self.program = defaultdict(int)
        self.screen = defaultdict(int)
        scores = []
        tiles = [" ", "|", "#", "=", "O"]
        positions = {"a": -1, "z": 0, "e": 1}
        for i, x in enumerate(program.strip().split(",")):
            self.program[i] = int(x)

        self.program[0] = 2

        self.relative_base = 0
        outputs = []
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
                self.draw_game()
                if cheat:
                    position = "z"
                    time.sleep(0.00005)
                else:
                    position = str(input())
                    position = position if position in positions.keys() else "z"
                self.program[self.get_index(i+1, opcode[2])] = positions[position]
                i += 2
            elif int(opcode[:2][::-1]) == 4:
                outputs.append(self.get_value(i+1, opcode[2]))
                i += 2
                if len(outputs) == 3:
                    if tuple(outputs[:2]) == (-1, 0):
                        scores.append(outputs[-1])
                    else:
                        self.screen[tuple(outputs[:2])] = tiles[outputs[-1]]
                    outputs = []
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

        return max(scores)


if __name__ == "__main__":
    with open("input_cheat.txt", "r") as f:
        program = f.read()
        print(CarePackage().main(program))
