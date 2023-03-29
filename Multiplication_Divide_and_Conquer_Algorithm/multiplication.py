def multi(a: int, b: int) -> int:
    # Pad the shorter number with zeros to make them the same length
    # Change the input to string before padding
    a_str = str(a)
    b_str = str(b)
    n = max(len(a_str), len(b_str))
    a_padded = a_str.zfill(n)
    b_padded = b_str.zfill(n)

    # Change the inputs back to int before doing the calculations
    a = int(a_padded)
    b = int(b_padded)

    if n > 1:
        k = int(n / 2)
        a1 = a // 10**k
        a0 = a - a1 * 10**k
        b1 = b // 10**k
        b0 = b - b1 * 10**k

        return (
            multi(a1, b1) * 10 ** (2 * k)
            + (multi(a1, b0) + multi(a0, b1)) * 10**k
            + multi(a0, b0)
        )
    return a * b


def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(f"{x} * {y} = {multi(x,y)}")


if __name__ == "__main__":
    main()
