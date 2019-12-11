from collections import defaultdict


class MonitoringStation:
    def is_detected(self, astro1, astro2):
        m = (astro2[1] - astro1[1]) / (astro2[0] - astro1[0]) if (astro2[0] != astro1[0]) else None
        for astro in self.astros:
            if astro == astro1 or astro == astro2:
                continue
            if m is None:
                if astro1[0] == astro[0] and (astro1[1] - astro[1]) * (astro2[1] - astro[1]) < 0:
                    return False
            else:
                # if the area of the formed triangle is 0, then collinear points (shoelace formula)
                in_line = astro1[0] * (astro2[1] - astro[1]) + astro2[0] * (astro[1] - astro1[1])
                in_line += astro[0] * (astro1[1] - astro2[1])
                if in_line == 0 and astro1[0] < astro[0] and astro[0] < astro2[0]:
                    return False

        return True

    def main(self, map_):
        map_ = list(map(list, map_.strip().split("\n")))
        monitored = defaultdict(list)
        self.astros = [(i, j) for i in range(len(map_[0])) for j in range(len(map_)) if map_[j][i] == '#']
        self.astros = sorted(self.astros, key=lambda x: x[0])

        for i, astro in enumerate(self.astros):
            for j in range(i+1, len(self.astros)):
                if self.is_detected(astro, self.astros[j]):
                    monitored[astro].append(self.astros[j])
                    monitored[self.astros[j]].append(astro)

        return max([len(x) for x in monitored.values()])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        map_ = f.read()
        print(MonitoringStation().main(map_))
