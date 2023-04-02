# # Lebinis formula
# # 4(1 - 1/3 + 1/5 - 1/7...)
def approximate_pi_leibniz(num_terms):
    pi_estimate = 0
    sign = 1
    for n in range(num_terms):
        term = sign / (2 * n + 1)
        pi_estimate += term
        sign *= -1
    pi_estimate *= 4
    return pi_estimate

print(approximate_pi_leibniz(1000000000))