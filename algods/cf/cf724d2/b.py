import math
def main():
    def nice(N, H):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        store = set()
        for i in H:
            store.add(i)
        # print(store)
        for i in alpha:
            if i not in store:
                return i
        i, j = 0, 0
        while j < len(alpha):
            two = alpha[i] + alpha[j]
            if two not in H:
                return two
            j += 1

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input()
            # H = input().split()
            # H = list(map(lambda x: int(x), H))
            print(nice(N, H))

    read_input()

if __name__ == "__main__":
    main()