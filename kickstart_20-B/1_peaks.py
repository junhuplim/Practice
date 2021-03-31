def main():
    def peaks(N, H):
        count = 0
        for i in range(1, N - 1):
            before, curr, after = H[i - 1], H[i], H[i + 1]
            count += 1 if (curr > before and curr > after) else 0
        return count

    def read_input():
        number_tests = int(input())
        for i in range(number_tests):
            N = int(input())
            H = input().split()
            H = list(map(lambda x: int(x), H))
            print(f'Case #{i + 1}: ', peaks(N, H))

    read_input()

if __name__ == "__main__":
    main()