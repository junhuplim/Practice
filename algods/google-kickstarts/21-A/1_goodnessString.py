def main():
    def goodness_string(arr, K):
        count = 0
        i, j = 0, len(arr) - 1
        while i < j:
            count += 1 if arr[i] != arr[j] else 0
            i += 1
            j -= 1

        return abs(K - count)

    def read_input():
        T = int(input())
        for i in range(T):
            N, K = input().split()
            arr = input()
            print(f'Case #{i + 1}: ', goodness_string(arr, int(K)))

    read_input()

if __name__ == "__main__":
    main()