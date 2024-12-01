def read(filename: str = 'input.txt', *, length: int = 1000, sort: bool = True):
    a_arr, b_arr = [0] * length, [0] * length
    with open(filename) as stream:
        for idx, line in enumerate(stream):
            if not line:
                continue
            a, b = line.strip().split()
            a_arr[idx], b_arr[idx] = int(a), int(b)
    if sort:
        a_arr.sort()
        b_arr.sort()
    return a_arr, b_arr


def main():
    a_arr, b_arr = read()
    res = sum(abs(a - b) for a, b in zip(a_arr, b_arr))
    print(res)


if __name__ == '__main__':
    main()