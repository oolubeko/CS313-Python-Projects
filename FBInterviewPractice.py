def allButI(a):
    for i in range(len(a)):
        product = 1
        for j in range(len(a)):
            if j != i:
                product *= a[j]
        print(product)

def get_max_profit(stock_y):
    max_prof = 0
    for i in range(len(stock_y)):
        buy = stock_y[i]
        j = i + 1
        while j < len(stock_y):
            sell = stock_y[j]
            if (sell - buy) > max_prof:
                max_prof = sell - buy
            j += 1
    return max_prof

def main():
    stock_y = [10,7,5,8,11,9]
    max_prof = get_max_profit(stock_y)
    print(str(max_prof))

main()
