def main():
    def record(arr):
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1

        curr_max, count = arr[0], 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i + 1] and arr[i] > curr_max:
                curr_max = arr[i]
                count += 1

        if arr[0] > arr[1]:
            count += 1
        if arr[-1] > curr_max:
            count += 1

        return count

    def read_input():
        T = int(input())
        for i in range(T):
            N = int(input())
            arr = [int(v) for v in input().split(" ")]
            arr = list(map(lambda x: int(x), arr))
            print(f'Case #{i + 1}: ', record(arr))

    read_input()

if __name__ == "__main__":
    main()