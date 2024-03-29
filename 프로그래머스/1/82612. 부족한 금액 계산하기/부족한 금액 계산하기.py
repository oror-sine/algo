def solution(price, money, count):
    fee = sum(range(count+1)) * price
    return 0 if money > fee else fee - money