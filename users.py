import datetime
from builtins import function
from dataclasses import dataclass

import self as self



class Contract:
    """The very same as smart-contract"""
    # remind and expire funs for event_loop

    CONTRACTS = []

    def __init__(self, contract_id, expires, price_rub, *parties):
        self.id = contract_id
        self.expires: datetime.date = expires
        self.price_rub: int = price_rub
        self.parties = [parties]
        Contract.CONTRACTS.append(self)


    # def remind(self, warning=False):
    #     if warning:
    #         return f"{self.__class__} {self.id} почти расторгнут!!!"
    #     else:
    #         return f"срок действия договора {self.id} скоро истечёт."
    # in bot.py main


    def __del__(self):
        #expires or break or occurance
        #where is Solidity????!!!!
        pass


@dataclass()
class Hypothec(Contract):

    def withdrawal(self):
        pass


@dataclass
class User:
    """Anyone who enters the bot area:
    borrowers, bank and insurence agents
    """
    money: int
    proof: bool           #licencies, passports, DNA signatures
    tg_id: str
    contracts: Contract = ()

def register(self, database):
    save_statement = f"INSERT INTO users(id, proof, role)" \
                     f"VALUES ({self.tg_id, self.proof, self.__class__})"
    database.do(save_statement)


    def proof(self):
        pass

    def view_contract(self):
        return self.contracts

    def pay(amount, reciever, *callback: function):
        self.money -= amount
        reciever.money += 0.99 * amount
        callback()


class Representer(User):
    contracts = ()
    companie_name: str


class Bank(Representer):

    def __init__(self):
        super().__init__()

    def resell(self, contract, acquirer: __init__):
        acquirer.contract.append(contract)
        self.contracts.remove(contract)


class InsuranceCompany(Representer):

    slogan = "/n Мы стали надёжней!!!"

    def __init__(self, companie_name):
        super(InsuranceCompany, self).__init__()
        self.ad = companie_name + self.slogan

    def wall_customers(self, ):
        #proposition to all customers
        pass



