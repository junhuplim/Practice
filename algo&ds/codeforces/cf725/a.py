import math
def main():
    def solve(N, H):
        min_idx = H.index(min(H))
        max_idx = H.index(max(H))
        if min_idx < max_idx:
            left_side = max_idx + 1
            right_side = N - min_idx
            both_side = min_idx + 1 + N - max_idx
        else:
            left_side = min_idx + 1
            right_side = N - max_idx
            both_side = max_idx + 1 + N - min_idx

        return min(left_side, right_side, both_side)

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(solve(N, H))

    read_input()

if __name__ == "__main__":
    main()