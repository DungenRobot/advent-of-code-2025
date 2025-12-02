import re



def main():


    with open("day02/input.txt") as f:
        line = f.read()

        ranges = line.split(',')

        total = 0

        for r in ranges:

            start, end = r.split('-')


            for x in range(int(start), int(end) + 1):

                l = len(str(x))

                if re.match('^(.+)\\1{1,}$', str(x)):
                    total += x
                
        print(total)







if __name__ == "__main__":
    main()