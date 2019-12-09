class ImageDecoder:
    def main(self, program):
        w, h = 25, 6
        image = list(map(int, list(program.strip())))
        rows = []
        for i in range(h):
            row = ''
            for j in range(w):
                pixels = [image[k] for k in range(i*w + j, len(image), w*h) if image[k] != 2]
                row += ' ' if pixels[0] == 0 else '#'
            rows.append(row)
        return '\n'.join(rows)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        program = f.read()
        print(ImageDecoder().main(program))
