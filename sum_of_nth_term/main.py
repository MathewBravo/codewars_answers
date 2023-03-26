def series_sum(n):
    div_by = 1
    sum = 0
    for i in range(n):
        sum += 1/div_by
        div_by += 3
    return "{:.2f}".format(sum)

if __name__ == "__main__":
    test = series_sum(1)
    print(test)
    if test == "1.39":
        print("pass")
    else:
        print("fail")

