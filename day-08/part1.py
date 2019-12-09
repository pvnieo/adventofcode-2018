import numpy as np


class ImageDecoder:
    def main(self, program):
        w, h = 25, 6
        image = list(map(int, list(program.strip())))
        layers = [image[i:i+w*h] for i in range(0, len(image), w*h)]
        index = np.argmin([layer.count(0) for layer in layers])
        return layers[index].count(1) * layers[index].count(2)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(ImageDecoder().main(program))
