def odd_gen():
    odd = 1
    while True:
        yield odd
        odd += 2


def pi_gen():
    my_odd_gen = odd_gen()
    index = 0
    next(my_odd_gen)
    series_sum = 1
    while True:
        yield series_sum
        odd = next(my_odd_gen)
        index += 1
        series_sum += (1 / odd) * (pow(-1, index))
        print(f"index: {index}, odd: {odd}, r: {series_sum}")


my_pi_gen = pi_gen()

# approximating pi using leibniz formula for pi

for i in range(100000):
    print(f"{next(my_pi_gen) * 4}")
