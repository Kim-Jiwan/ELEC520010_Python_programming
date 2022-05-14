# 2017110292 김지완

class BankAccount:
    def __init__(self, name, account_num, balance = 0):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance

    def __str__(self):
        return f"{self.__name}님의 계좌 {self.__account_num}의 잔고는 {self.__balance:,d}원 입니다."

    def get_name(self):
        return self.__name

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        self.__balance += money
        print(f"{money:,d}원이 입금되었습니다. 잔고는 {self.__balance:,d}원입니다.")

    def withdraw(self, money):
        if self.__balance < money:
            print(f"계좌 잔고는 {self.__balance:,d}원으로 인출 요구 금액 {money:,d}원보다 작습니다.")
        else:
            self.__balance -= money

my_account = BankAccount("김지완", "5819-0924")
print(my_account)
my_account.deposit(2000)
print(my_account)
my_account.withdraw(500)
print(my_account)
my_account.withdraw(5000)