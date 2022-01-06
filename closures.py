def make_division_by(n):
    assert isinstance(n, (int, float)), "debe ser numérico"
    def division(x):
        assert isinstance(x, (int, float)), "debe ser numérico"
        return int(x / n)
    return division

division_by_3 = make_division_by(5)
print(division_by_3(18))