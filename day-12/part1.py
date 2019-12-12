from itertools import combinations


class MotionSimulator:
    def main(self, coord):
        coord = [list(map(lambda x: int(x.strip()[2:]), x[1:-1].split(','))) for x in coord.strip().split("\n")]
        velocity = [[0, 0, 0] for _ in range(len(coord))]

        for _ in range(1000):
            # update velocity
            for i, j in combinations(range(len(coord)), 2):
                for k in range(3):
                    step = (coord[j][k] - coord[i][k]) and (1, -1)[(coord[j][k] - coord[i][k]) < 0]
                    velocity[i][k] += step
                    velocity[j][k] -= step
            # update position
            coord = [[a+b for a, b in zip(x, velocity[i])] for i, x in enumerate(coord)]

        # compute total energy
        return sum([sum(map(abs, coord[i])) * sum(map(abs, velocity[i])) for i in range(len(coord))])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        coord = f.read()
        print(MotionSimulator().main(coord))
