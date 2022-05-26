import sys

class Bank:
    def __init__(self):
        self.data = {}
    
    def add_user(self, user_id, user_name, card_num, pin):
        self.data[user_id] = {"USER_NAME":user_name ,"CARD_NUM": card_num, "PIN": pin, "ACCOUNTS":{}}

    def add_account(self, user_id, account, balance):
        if user_id in self.data:
            self.data[user_id]["ACCOUNTS"][account] = balance
        else:
            pass

    def check_num(self, card_num):
        for user_id, user_info in self.data.items():
            if user_info["CARD_NUM"] == card_num:
                return True
        return False

    def get_id(self, card_num):
        for user_id, user_info in self.data.items():
            if user_info["CARD_NUM"] == card_num:
                return user_id

    def check_pin(self, user_id, pin): 
        if self.data[user_id]["PIN"] == pin:
            return True
        else:
            return False
    
    def get_accounts(self, user_id):
        return self.data[user_id]["ACCOUNTS"]

    # test
    def get_users(self):
        return self.data

class ATMController:
    def __init__(self, bank):
        self.Bank = bank
        self.cash_bin = None
        self.user_id = None
        self.accounts = None
        self.account = None

    def insert_card(self, card_num):
        if self.Bank.check_num(card_num):
            self.user_id = self.Bank.get_id(card_num)
            return True
        else:
            return False
    
    def insert_pin(self, pin):
        if self.Bank.check_pin(self.user_id, pin):
            self.accounts = self.Bank.get_accounts(self.user_id)
            return True
        else:
            return False

    def select_account(self, account):
        if account in self.accounts:
            self.account = account
            return True
        else:
            return False
    
    def see_balance(self):
        return self.Bank.data[self.user_id]["ACCOUNTS"][self.account]

    def deposit(self, cash):
        self.cash_bin = cash
        self.Bank.data[self.user_id]["ACCOUNTS"][self.account] += cash
        self.cash_bin = 0
        return True
    
    def withdraw(self, cash):
        if self.Bank.data[self.user_id]["ACCOUNTS"][self.account] >= cash:
            self.Bank.data[self.user_id]["ACCOUNTS"][self.account] -= cash
            self.cash_bin = cash
            self.cash_bin = 0
            return True
        else:
            return False

if __name__ == "__main__":
    if sys.version_info < (3,10,2):
        sys.exit()

    test_bank = Bank()

    # Adding test accounts
    test_bank.add_user(322480019, "John Doe", 4716769242153267, 2584)
    test_bank.add_account(322480019, "Savings", 5000)
    test_bank.add_account(322480019, "Checking", 300)
    test_bank.add_user(460061427, "Jane Doe", 4916207774529883, 7758)
    test_bank.add_account(460061427, "Savings", 40000)
    test_bank.add_account(460061427, "Checking", 3200)
    test_bank.add_user(339546546, "Lorem Ipsum", 4532770757460503, 1507)
    test_bank.add_account(339546546, "Savings", 100000)
    test_bank.add_account(339546546, "Checking", 30)
    test_bank.add_user(968675287, "Dolor Sit", 4916222412454790, 5062)
    test_bank.add_account(968675287, "Checking", 4)
    test_bank.add_user(282912512, "Amet Consectetur", 4916354376907529, 3961)
    test_bank.add_account(282912512, "Checking", 4560)
    
    print (test_bank.get_users())

    # Testing ATM
    test_atm = ATMController(test_bank)
    assert test_atm.insert_card(4716769242153267) == True
    assert test_atm.insert_card(5492767304512872) == False
    assert test_atm.insert_card(4916207774529883) == True
    assert test_atm.insert_card(5365127081758228) == False
    assert test_atm.insert_card(0000000000000000) == False

    test_atm.insert_card(4916354376907529)
    assert test_atm.insert_pin(3961) == True
    assert test_atm.insert_pin(0000) == False
    test_atm.insert_card(4916222412454790)
    assert test_atm.insert_pin(5062) == True
    assert test_atm.insert_pin(2040) == False
    test_atm.insert_card(4916207774529883)
    assert test_atm.insert_pin(9999) == False

    test_atm.insert_card(4916354376907529)
    assert test_atm.select_account("Checking") == True
    assert test_atm.select_account("Savings") == False
    test_atm.insert_card(4916222412454790)
    assert test_atm.select_account("Checking") == True
    assert test_atm.select_account("Savings") == False
    test_atm.insert_card(4716769242153267)
    assert test_atm.select_account("An Invalid Account") == False

    test_atm.insert_card(4716769242153267)
    test_atm.select_account("Checking")
    assert test_atm.see_balance() == 300
    assert test_atm.deposit(61) == True
    assert test_atm.withdraw(10000) == False
    assert test_atm.withdraw(299) == True

    print ("Everything passed")