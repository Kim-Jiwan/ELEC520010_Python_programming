def unit_fracation(frac):
    i = 2

    if frac > 0.5:
        return 1 / 2
    else:
        while frac < 1 / i:
            i += 1

        if (1 / i) - frac > frac - (1 / (i + 1)):
            return 1 / (i + 1)
        else:
            return 1 / i

N = float(input("1보다 작고 0보다 큰 소수를 입력하세요 : "))

print(f"가장 가까운 단위 분수는 1/{int(1 / unit_fracation(N))} 이며, 이 값은 {unit_fracation(N)}입니다.")