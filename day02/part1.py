



def main():
    with open("day02/input.txt") as f:
        line = f.read()

        ranges = line.split(',')

        total = 0

        for r in ranges:

            start, end = r.split('-')


            for x in range(int(start), int(end) + 1):

                l = len(str(x)) // 2

                if str(x)[:l] == str(x)[l:]:
                    total += x
        print(total)







if __name__ == "__main__":
    main()