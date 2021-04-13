def main():
    def countdown(arr, N, K):
        i, temp, count = 0, 0, 0
        for i in range(1, N):
            if arr[i - 1] == arr[i] + 1:
                temp += 1
            else:
                temp = 0
            if arr[i] == 1 and temp >= K - 1:
                count += 1

        return count

    def read_input():
        T = int(input())
        for i in range(T):
            temp = input().split()
            N, K = int(temp[0]), int(temp[1])
            arr = input().split()
            arr = list(map(lambda x: int(x), arr))
            print(f'Case #{i + 1}: ', countdown(arr, N, K))

    read_input()

if __name__ == "__main__":
    main()