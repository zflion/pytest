# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import picSort

import speedTestPrint
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    addWithPrompt()
    #speedTestPrint.printCurrentSpeed()


def addWithPrompt():
    a,b = (input("请输入两个数字,以空格隔开:").split())
    a = float(a)
    b = float(b)
    print(f'{a}+{b}={a+b}')
    input('end')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello ZSN!!')
    #picSort.print_pic_by_cration_time('D:\PIC')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
