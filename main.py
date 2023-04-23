# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import picSort

import speedTestPrint
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    addWithPrompt()
    # speedTestPrint.printCurrentSpeed()


def addWithPrompt():
    prompt = input("请输入两个数字,以空格隔开, 退出请输入 q:")
    while prompt != 'q':
        inputCorrect = False
        try:
            a, b = (prompt.split())
            inputCorrect = True
        except:
            print("输入错误！")

        if inputCorrect:
            a = float(a)
            b = float(b)
            print(f'{a}+{b}={a + b}')

        prompt = input("请输入两个数字,以空格隔开, 退出请输入 q:")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello ZSN!!')
    # picSort.print_pic_by_cration_time('D:\PIC')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
