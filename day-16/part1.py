from itertools import cycle


class FlawedFrequencyTransmission:
    def main(self, signal):
        signal = list(map(int, signal.strip()))
        pattern = {}
        for i in range(len(signal)):
            pattern_cycle = cycle([0, 1, 0, -1])
            pattern[i] = sum([[next(pattern_cycle)] * (i+1) for _ in range(len(signal) // (i+1) + 2)], [])
            pattern[i] = pattern[i][1:len(signal)+1]

        for _ in range(100):
            signal_copy = signal.copy()
            for i in range(len(signal)):
                signal[i] = int(str(sum([x * pattern[i][j] for j, x in enumerate(signal_copy)]))[-1])

        return int("".join(map(str, signal))[:8])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        signal = f.read()
        print(FlawedFrequencyTransmission().main(signal))
