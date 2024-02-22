from gcd import gcd


def test_gcd():
    n = 3
    m = 15
    d = gcd(n, m)

    assert d > 0  # 1) `d` is positive
    assert n % d == 0  # 2) `d` divides `n`
    assert m % d == 0  # 3) `d` divides `m`

    # 4) no other number larger than `d` divides both `n` and `m`
    for i in range(d + 1, min(n, m)):
        assert (n % i) or (m % i)
