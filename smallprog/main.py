# This is a sample Python script. falk edit

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print('Какую программу запустить:')
print('1 - калькулятор')
print('2 - угадай число')
print('3 - улятор')
print('4 - список дел')
print('0 - ВЫХОД')

while True:
    guess = int(input("Input prog: "))
    if guess == 1:
        print("RUN calk")
    elif guess == 2:
        print("RUN ugad")
    elif guess == 3:
        print("RUN rand")
    elif guess == 4:
        print("RUN todo")
    elif guess == 0:
        print("Congratulations!")
        break

