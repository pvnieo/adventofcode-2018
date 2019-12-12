import threading
import time
from itertools import permutations


class AmplifierController:
    def get_value(self, index, mode, program):
        if mode == "0":
            return program[program[index]]
        return program[index]

    def run_program(self, program, I):
        i = 0
        while i < len(program):
            opcode = str(program[i])[::-1] + '0' * (5 - len(str(program[i])))
            if int(opcode[:2][::-1]) == 99:
                self.outputs[I] = self.queues[(I+1) % 5]
                return
            elif int(opcode[:2][::-1]) == 1:
                program[program[i+3]] = self.get_value(i+1, opcode[2], program) + self.get_value(i+2, opcode[3], program)
                i += 4
            elif int(opcode[:2][::-1]) == 2:
                program[program[i+3]] = self.get_value(i+1, opcode[2], program) * self.get_value(i+2, opcode[3], program)
                i += 4
            elif int(opcode[:2][::-1]) == 3:
                while not self.queues[I]:
                    time.sleep(0.0000001)
                program[program[i+1]] = self.queues[I].pop(0)
                i += 2
            elif int(opcode[:2][::-1]) == 4:
                self.queues[(I+1) % 5].append(self.get_value(i+1, opcode[2], program))
                i += 2
            elif int(opcode[:2][::-1]) == 5:
                i = self.get_value(i+2, opcode[3], program) if self.get_value(i+1, opcode[2], program) != 0 else i + 3
            elif int(opcode[:2][::-1]) == 6:
                i = self.get_value(i+2, opcode[3], program) if self.get_value(i+1, opcode[2], program) == 0 else i + 3
            elif int(opcode[:2][::-1]) == 7:
                program[program[i+3]] = 1 if self.get_value(i+1, opcode[2], program) < self.get_value(i+2, opcode[3], program) else 0
                i += 4
            elif int(opcode[:2][::-1]) == 8:
                program[program[i+3]] = 1 if self.get_value(i+1, opcode[2], program) == self.get_value(i+2, opcode[3], program) else 0
                i += 4
            else:
                raise("Invalid opcode: {}".format(opcode))

    def run_simulation(self, program, phase_settings):
        self.outputs, threads = {}, {}
        self.queues = {i: [x] for i, x in enumerate(phase_settings)}
        self.queues[0].append(0)
        for i in range(5):
            thr = threading.Thread(target=self.run_program, args=(program.copy(), i))
            threads[i] = thr
            thr.start()

        for i in range(5):
            threads[i].join()
        return self.outputs[4][0]

    def main(self, program):
        program = list(map(int, program.strip().split(",")))
        phase_settings = permutations(range(5, 10), 5)
        return max([self.run_simulation(program.copy(), phase_setting) for phase_setting in phase_settings])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(AmplifierController().main(program))
