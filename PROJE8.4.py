class Account:
    accounts = [] 

    def __init__(self, account_number, owner, balance=0.0):
        self.__account_number = account_number  
        self.__owner = owner  
        self.__balance = balance  
        Account.accounts.append(self)  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  
            Bank.track_transaction(f"{self.__owner} hesabına {amount} yatırıldı.")
            print(f"{amount} TL yatırıldı. Yeni bakiye: {self.__balance} TL")
        else:
            print("Yatırılan miktar sıfırdan büyük olmalıdır.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount  
                Bank.track_transaction(f"{self.__owner} hesabından {amount} çekildi.")
                print(f"{amount} TL çekildi. Yeni bakiye: {self.__balance} TL")
            else:
                print("Yetersiz bakiye.")
        else:
            print("Çekilen miktar sıfırdan büyük olmalıdır.")

    def view_balance(self):
        print(f"Hesap Sahibi: {self.__owner}, Hesap Numarası: {self.__account_number}, Bakiyeniz: {self.__balance} TL")

class Bank:
    transaction_history = []  

    def display_bank_info():
        print("Banka Bilgileri:")
        print("Banka adı: Akıllı Banka")
        print("Müşteri memnuniyeti önceliğimizdir.")
    
    
    def track_transaction(description):
        Bank.transaction_history.append(description)  

    
    def display_transaction_history():
        print("İşlem Geçmişi:")
        for transaction in Bank.transaction_history:
            print(transaction)


def main():
    while True:
        print("\n--- Banka Hesap Yönetim Sistemi ---")
        print("1. Hesap Oluştur")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Görüntüle")
        print("5. Banka Bilgileri Göster")
        print("6. İşlem Geçmişini Göster")
        print("0. Çıkış")
        choice = input("Seçiminizi yapın: ")

        if choice == '0':
            break
        elif choice == '1':
            account_number = input("Hesap numarasını girin: ")
            owner = input("Hesap sahibinin adını girin: ")
            new_account = Account(account_number, owner)
            print(f"{owner} için hesap oluşturuldu.")
        elif choice == '2':
            account_number = input("Para yatırılacak hesap numarasını girin: ")
            amount = float(input("Yatırılacak miktarı girin: "))
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '3':
            account_number = input("Para çekilecek hesap numarasını girin: ")
            amount = float(input("Çekilecek miktarı girin: "))
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '4':
            account_number = input("Bakiyesi görüntülenecek hesap numarasını girin: ")
            for account in Account.accounts:
                if account._Account__account_number == account_number:
                    account.view_balance()
                    break
            else:
                print("Hesap bulunamadı.")
        elif choice == '5':
            Bank.display_bank_info()
        elif choice == '6':
            Bank.display_transaction_history()
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
