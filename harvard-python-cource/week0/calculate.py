x = float(input("What's X? "))
y = float(input("What's Y? "))

z = round(x / y, 3)

# round() округляет число до n знаков после запятой

z = x / y
print(f"{z:.2f}")

# округление через :.nf

def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))

def square(n):
    return pow(n, 2)

# pow() возводит число n в i степень

main()