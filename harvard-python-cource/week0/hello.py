# Ask user for their name
name = input("What's your name? ").strip().title()

# strip() удаляет лишние пробелы
# title() делает первую букву заглавной во всех словах
# capitalize() делает первую букву заглавной в первом слове

# Say hello to user
print("Hello,", name, sep=' ', end='\n')

print("Hello, \"friend\"")

def hello(to="world"):
    print("Hello", to)

hello(name)