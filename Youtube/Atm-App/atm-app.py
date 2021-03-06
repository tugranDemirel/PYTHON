"""
    ATM APPLICATION
"""

# data and structre
accountOne = {
    'name' : 'tugran',
    'accountNum' : '123456789',
    'totalMoney' : 0,
    'exMoney' : 3000
}

accountTwo = {
    'name' : 'kadir',
    'accountNum' : '987654321',
    'totalMoney' : 0,
    'exMoney' : 3000
}

def getMoney(accountName, amountMoney):
    '''
        DOCSTRING: Get money function
        INPUT: Acoount name and take to money
        OUTOUT: Account information
    '''
    if(accountName['totalMoney'] >= amountMoney):
        print(f"Take to money: {amountMoney}") # çekilen tutar
        print(f"Your remaining balance: {accountName['totalMoney'] - amountMoney}") # kalan bakiyeniz.
        accountName['totalMoney'] = accountName['totalMoney'] - amountMoney
    else:
        confirm = input("your don't have enough money in your main account . Do you take to money extra balance?(y/n)\n")
        # Ana hesabınızda yeterli bakiye kalmamıştır. Ek bakiyeden çekmek ister misiniz ?
        if ((confirm == 'y') or (confirm == 'Y')):
            if((accountName['totalMoney'] + accountName['exMoney']) >= amountMoney ): # hesaptaki toplam bakiye çekilecek tutardan fazla ise
                accountName['exMoney'] = accountName['exMoney'] + (accountName['totalMoney'] - amountMoney)
                print(f"Money Withdram: {amountMoney}\nYour money withdraw extra balance: {accountName['exMoney']}\n")
                accountName['totalMoney'] = 0
            else:
                print("You don't have enough money in your acoount")
        elif((confirm == 'n') or (confirm == 'N')):
            print("CANCELED")

def setMoney(accountName, amountMoney):
    '''
        DOCSTRING: Set money function
        INPUT: Acoount name and set to money
        OUTOUT: Account information
    '''
    if(accountName['exMoney'] < 3000): # ek hesap kullanılmış ise hesaba yatırılan paradan ilk ek hesap limiti sıfırlanacak
        accountName['exMoney'] +=  amountMoney
        remainingBalance = accountName['exMoney'] - 3000
        accountName['exMoney'] -= remainingBalance
        print("Update Extra Balance.\nExtra Balance {0:}".format(accountName['exMoney']))
        accountName['totalMoney'] += remainingBalance
        print("Update Main Balance.\nMain Balance {0:}".format(accountName['totalMoney']))
    else:
        print("Remaining Balance Updating\n")
        accountName['totalMoney'] = accountName['totalMoney'] + amountMoney
        print("Update.\nNew Balance: {0:}".format(accountName['totalMoney']))

def setLimit(accountName):
    '''
        DOCSTRING: Extra Balance Limit Setting
        INPUT: Acoount name
        OUTOUT: Account Extra Balance Limit
    '''
    print(f"Limit: {accountName['exMoney']}")
    limit = int(input("Enter the extra balance limit: "))
    accountName.update({"exMoney": limit}) # limit güncelleme işlemi. "accountName['exMoney'] = limit" şeklinde de yapılabilir.
    print("UPDATING.")
    print(f"Extra Balance Limit: {accountName['exMoney']}")
