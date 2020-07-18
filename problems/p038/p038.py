from itertools import permutations


def main():
    """
    Find some number n that when multipled by every element in an array
    (1, 2, ..., a) where a > 1


    Limitations:
      * Must have 9 digits
      * Each digit between 1 - 9 must appear once and only once
    """
    successes = []
    for canidate in permutations("987654321"):
        canidate = concat(canidate)
        for i in [1, 2, 3]:  # If n needs the 5th index n * 2 will take up 10 digits
            n = int(canidate[:i])
            poss =  concat([a * n for a in range(1, i + 1)])
            if poss == canidate:
                successes.append(canidate)
    return successes


def concat(arr):
    result = ""
    for e in arr:
        result += str(e)
    return result


if __name__ == "__main__":
    print(main())
