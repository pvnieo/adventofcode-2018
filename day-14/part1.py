from math import ceil
from collections import defaultdict


class SpaceStoichiometry:
    def main(self, reactions):
        rea = reactions.strip().split("\n")
        reactions = [[[(int(e.split()[0]), e.split()[1]) for e in s.split(", ")] for s in l.strip().split(' => ')] for l in rea]
        reactions = {r[1][0][1]: (int(r[1][0][0]), r[0]) for r in reactions}

        need = defaultdict(int)
        need["FUEL"] = 1
        while True:
            try:
                ele, qt = next(((el, qt) for el, qt in need.items() if qt > 0 and el != "ORE"))
            except Exception:
                break
            ele_coef, ingreds = reactions[ele]
            factor = ceil(qt / ele_coef)
            for n_coef, n_name in ingreds:
                need[n_name] += n_coef * factor
            need[ele] -= factor * ele_coef

        return need["ORE"]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        reactions = f.read()
        print(SpaceStoichiometry().main(reactions))
