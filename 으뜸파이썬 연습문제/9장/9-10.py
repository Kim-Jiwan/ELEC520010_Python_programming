class BankAccount:

    def __init__(self, name, account_num, balance = 0):
        self.__name = name
        self.__account_num = account_num
        self.__balance = balance

    def __str__(self):
        return f"{self.__name}님의 계좌 {self.__account_num}의 잔고는 {self.__balance:,d}원입니다."
    
    def merge_account(self, account):
        return BankAccount(self.__name, self.__account_num, self.__balance + account.__balance)

    def get_name(self):
        return self.__name

    def get_account_num(self):
        return self.__account_num

    def get_balance(self):
        return self.__balance

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance >= money:
            self.__balance -= money
        else:
            print(f"계좌 잔고는 {self.__balance:,d}원으로 인출 요구 금액 {money:,d}원보다 작습니다.")
        
my_account = BankAccount("김지완", "3333064530707", 100000)
my_account1 = BankAccount("김지완", "1", 300000)
print(my_account)

new_account = BankAccount.merge_account(my_account, my_account1)
print(new_account)

new_account.deposit(4000000)
print(new_account)
new_account.withdraw(500000000)