if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uarr=list(set(arr))
    uarr.sort()
    print(uarr[-2])
