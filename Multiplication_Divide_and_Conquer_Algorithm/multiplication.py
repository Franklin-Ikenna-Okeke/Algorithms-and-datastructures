def multi(a: int, b: int) -> int:
    # Pad the shorter number with zeros to make them the same length
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)

    k = int(n / 2)
    a1 = a / 10 ^ k
    a0 = a - a1 * 10 ^ k


def main():
    x = input("Enter first number")
    y = input("Enter second number")
    print(f"{x} * {y} = {multi(x,y)}")


if __name__ == "__main__":
    main()
