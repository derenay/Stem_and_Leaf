import random


class Side_by_side_Stem_and_leaf():
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def data_matrix(self):
        for i, x in enumerate(sorted(self.data1)):
            print(f"{x:4d}", end="")
            if (i + 1) % 10 == 0:
                print("")
        print("\n\n\n\n")
        for i, x in enumerate(sorted(self.data2)):
            print(f"{x:4d}", end="")
            if (i + 1) % 10 == 0:
                print("")

    def stem_and_leaf(self, stems):
        print("")
        for s in stems:
            v = [str(n - s[0]) for n in sorted(self.data1) if n >= s[0] and n <= s[1]]
            t = [str(i - s[0]) for i in sorted(self.data2) if i >= s[0] and i <= s[1]]
            v_str = " ".join(v)
            t_str = " ".join(t)
            print(f"{t_str.rjust(80)} | {s[0] // 10} | {v_str}")


def main():
    data1 = [random.randint(10, 99) for _ in range(100)]

    data2 = [random.randint(10, 99) for _ in range(100)]
    stems = [
        (10, 19),
        (20, 29),
        (30, 39),
        (40, 49),
        (50, 59),
        (60, 69),
        (70, 79),
        (80, 89),
        (90, 99)
    ]

    side_by_side_Stem_and_leaf = Side_by_side_Stem_and_leaf(data1, data2)
    print(side_by_side_Stem_and_leaf.stem_and_leaf(stems))


if __name__ == "__main__":
    main()
