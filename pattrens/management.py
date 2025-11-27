#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Account:
    def view_stock(self):
        print("Viewing stock")

    def purchase(self):
        print("Making a purchase")

    def place_order(self):
        print("Placing an order")

class ManagerAccount(Account):
    def permissions(self):
        return ["manage_stock", "make_purchases", "view_income"]

class SellerAccount(Account):
    def permissions(self):
        return ["sell", "make_purchases", "place_orders"]

class VisitorAccount(Account):
    def permissions(self):
        return ["view_stock", "place_orders"]

class AccountFactory:
    @staticmethod
    def create_account(role):
        role = role.lower()
        if role == "manager":
            return ManagerAccount()
        elif role == "seller":
            return SellerAccount()
        elif role == "visitor":
            return VisitorAccount()
        else:
            raise ValueError("Unknown role: " + role)

if __name__ == "__main__":
    for r in ["manager", "seller", "visitor"]:
        acc = AccountFactory.create_account(r)
        print(f"\nTesting {r.capitalize()} Account:")
        acc.view_stock()
        acc.purchase()
        acc.place_order()
        print("Permissions:", acc.permissions())
