def main():
    def solve(arr):
        red, blue, a, b = arr
        if a == b:
            ans = min(red, blue) // a
        else:
            ans = helper(red, blue, a, b, 0)
        return ans

    def helper(red, blue, a, b, count):
        if red > blue:
            if a >= b:
                if red < a or blue < b:
                    return count
                else:
                    return helper(red-a, blue-b, a, b, count + 1)
            else:
                if red < b or blue < a:
                    return count
                else:
                    return helper(red-b, blue-a, a, b, count + 1)
        else:
            if a >= b:
                if blue < a or red < b:
                    return count
                else:
                    return helper(red-b, blue-a, a, b, count + 1)
            else:
                if blue < b or red < a:
                    return count
                else:
                    return helper(red-a, blue-b, a, b, count + 1)



    number_tests = int(input())
    for _ in range(number_tests):
        arr = list(map(int, input().split()))
        print(solve(arr))

if __name__ == "__main__":
    main()