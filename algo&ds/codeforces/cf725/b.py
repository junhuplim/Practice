import math
def main():
    def solve(N, H):
        sorted_arr = sorted(H)
        if (sum(H) % N) != 0:
            return -1
        avg = sum(H) / N
        count = 0
        for i in H:
            if i > avg:
                count += 1

        return count

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            # H = input()
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(solve(N, H))

    read_input()

if __name__ == "__main__":
    main()