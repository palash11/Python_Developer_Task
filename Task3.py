import os


def _randbelow(n):
    """Return a random int in the range [0,n).  Raises ValueError if n<=0."""
    # from Lib/random.py
    if n <= 0:
        raise ValueError
    k = n.bit_length()  # don't use (n-1) here because n can be 1
    r = getrandbits(k)          # 0 <= r < 2**k
    while r >= n:  # avoid skew
        r = getrandbits(k)
    return r


def shuffle(bias_list):
    """shuffle list"""
    shuffled_list = []
    for _ in xrange(len(bias_list)):
        element = bias_list[randint(0, len(bias_list)-1)]
        bias_list.remove(element)
        shuffled_list.append(element)

    return shuffled_list


def getrandbits(k):
    """getrandbits(k) -> x.  Generates an int with k random bits."""
    if k <= 0:
        raise ValueError('number of bits must be greater than zero')
    if k != int(k):
        raise TypeError('number of bits should be an integer')
    numbytes = (k + 7) // 8  # bits / 8 and rounded up
    x = int(os.urandom(numbytes).encode('hex'), 16)
    return x >> (numbytes * 8 - k)


def randint(low, high):
    """Return random integer in range [low, high], including both end points."""
    return low + _randbelow(high - low + 1)


def main():
    """script starts from this function"""
    # population containers
    result = []
    high_list = []
    low_list = []

    # number of time to generate
    times_to_run = 100
    # percentage bias towards higher value
    biased_to_high = 73

    # lowest, mid and highest excepted values must be integer
    lowest_value = 1
    mid_value = 5
    highest_value = 10

    biased_to_low = 100.0 - biased_to_high

    if lowest_value >= mid_value or lowest_value >= highest_value:
        raise ValueError("Lowest value is not the lowest between mid value and high value")
    elif mid_value > highest_value:
        raise ValueError("Mid value is higher that highest value")

    if biased_to_high < 0 or biased_to_high > 100:
        raise ValueError("Percentage of bias must be between 0 to 100")

    while len(high_list) < round(times_to_run*(biased_to_high/100.0)) or \
            len(low_list) < round(times_to_run*(biased_to_low/100.0)):

        # generate all random values
        if len(high_list) < round(times_to_run*(biased_to_high/100.0)) and \
                len(low_list) < round(times_to_run * (biased_to_low / 100.0)):
            num = randint(lowest_value, highest_value)
        # generate only high random value as low is exhausted
        elif len(low_list) == round(times_to_run * (biased_to_low / 100.0)):
            num = randint(mid_value, highest_value)
        # generate only low random value as high is exhausted
        elif len(high_list) == round(times_to_run*(biased_to_high/100.0)):
            num = randint(lowest_value, mid_value-1)

        if num >= mid_value:
            high_list.append(num)
        else:
            low_list.append(num)

    # shuffle the final result population of low and high as these are separate and distinguishable values
    result = shuffle(high_list+low_list)  # randomize population but time consuming

    print("Number of low values:  {:>5}".format(len(low_list)))
    print("Number of high values: {:>5}".format(len(high_list)))
    print("Total population:      {:>5}".format(len(result)))
    print(result[:100])
    print(low_list)
    print(high_list)
    print('_'*120)


if __name__ == "__main__":
    main()
