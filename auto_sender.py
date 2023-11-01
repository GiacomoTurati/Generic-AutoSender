#import zone
import pyautogui, keyboard, time, random, string, os

#ignore this
letters = string.ascii_letters
digits = string.digits
spam = letters + digits
os.system("cls")

#autosender
def auto_sender():
    os.system("cls")
    print("AUTO SENDER\n")
    auto_sender = open("spam.txt","r", encoding='utf-8')
    print("starting in 3 seconds...")
    for i in range(4,1,-1):
        print(i-1)
        time.sleep(1)
    print("starting...")

    with open('spam.txt', encoding='utf-8') as f: 
        for i in f:
            keyboard.write(i, delay=0.2)
            pyautogui.press("enter")
            time.sleep(1)

#spam
def spam1():
    os.system("cls")
    print("GENERAL SPAM\n")
    spam_fast = float(input("how much time passes between each message? "))
    random_message = input("do you whant to chose the message to spam? yes/no ")
    if random_message == "yes":
        message = input("what message do you whant to spam? ")
        print("i will print" + str(message) + "every " + str(spam_fast) + "seconds")
        print("starting in 3 seconds...")
        for i in range(4,1,-1):
            print(i-1)
            time.sleep(1)
        print("starting...")
        while True:
            keyboard.write(message)
            pyautogui.press("enter")
            time.sleep(spam_fast)
    else:
        message = input("what message do you whant to spam? ")
        print("i will print" + str(message) + "every " + str(spam_fast) + "seconds")
        print("starting in 3 seconds...")
        for i in range(4,1,-1):
            print(i-1)
            time.sleep(1)
        print("starting...")
        while True:
            keyboard.write(message)
            pyautogui.press("enter")
            time.sleep(secret.chose(spam))

#numbers spam
def numbers_auto_sender():
    os.system("cls")
    print("NUMBERS AUTO SENDER\n")
    start_num = int(input("Insert the starting number: "))
    for i in range(4,1,-1):
        print(i-1)
        time.sleep(1)
    print("starting...")
    while True:
        keyboard.write(str(start_num))
        pyautogui.press("enter")
        start_num = start_num + 1
        time.sleep(2)

while True:
    print("What option you want to run? \n1) auto_sender\n2) spam\n3) numbers_auto_sender\n")
    run = input()
    if run == "auto_sender" or run == "1":
        auto_sender()
        break
    elif run == "spam" or run == "2":
        spam1()
        break
    elif run == "numbers_auto_sender" or run == "3":
        numbers_auto_sender()
        break
    else:
        print(r"error please rety (the option are: 1,2,3)")