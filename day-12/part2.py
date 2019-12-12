import math
from itertools import combinations


class MotionSimulator:
    def lcm(self, a, b):
        return abs(a*b) // math.gcd(a, b)

    def main(self, coord):
        coord = [list(map(lambda x: int(x.strip()[2:]), x[1:-1].split(','))) for x in coord.strip().split("\n")]
        init_coord = coord.copy()
        velocity = [[0, 0, 0] for _ in range(len(coord))]
        frequencies = []

        for k in range(3):
            count = 0
            while True:
                # update velocity
                for i, j in combinations(range(len(coord)), 2):
                    step = (coord[j][k] - coord[i][k]) and (1, -1)[(coord[j][k] - coord[i][k]) < 0]
                    velocity[i][k] += step
                    velocity[j][k] -= step
                # update position
                coord = [[a+b for a, b in zip(x, velocity[i])] for i, x in enumerate(coord)]
                count += 1

                if [x[k] for x in velocity] == [0, 0, 0, 0] and [x[k] for x in coord] == [x[k] for x in init_coord]:
                    frequencies.append(count)
                    break

        return self.lcm(self.lcm(*frequencies[:2]), frequencies[-1])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        coord = f.read()
        print(MotionSimulator().main(coord))
