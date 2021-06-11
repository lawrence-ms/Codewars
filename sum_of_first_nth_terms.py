# https://www.codewars.com/kata/555eded1ad94b00403000071

def series_sum(n):
    sum = 0.00
    for i in range(n):
        sum += 1 / (4 + 3 * (i - 1))
    return "{:.2f}".format(sum)
