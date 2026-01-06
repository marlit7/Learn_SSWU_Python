# --------------------------- Homework_6.2  ------------------------------------
# SRP

# accounts_list = []
#
# class BankAccount:
#     def __init__(self, account_no: str):
#         self.account_no = account_no
#
#     def get_account_number(self):
#         return self.account_no
#
#     def save(self) -> None:
#         accounts_list.append(self)
#         print("Success, saved to DB")
#

accounts_list = []

class BankAccount:
    def __init__(self, account_no: str):
        self.account_no = account_no

    def get_account_number(self):
        return self.account_no


class AccountRepository:
    def save(self, account: BankAccount) -> None:
        accounts_list.append(account)
        print("Success, saved to DB")


