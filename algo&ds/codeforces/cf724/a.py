import math
def main():
    def nice(N, H):
        neg = False
        for i in H:
            if i < 0:
                print('no')
                neg = True
                break
        if not neg:
            print('yes')

            highest = max(H)
            if 0 in H:
                print(highest + 1)
                for i in range(highest + 1):
                    print(i, end=" ")
            else:
                print(highest)
                for i in range(1, highest + 1):
                    print(i, end=" ", flush=True)

            print('')


    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input().split()
            H = list(map(lambda x: int(x), H))
            # print(nice(N, H))
            nice(N, H)

    read_input()

if __name__ == "__main__":
    main()