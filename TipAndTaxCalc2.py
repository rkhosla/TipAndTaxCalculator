#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:02:03 2018

@author: armyresearch
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 08:27:55 2018

@author: armyresearch
"""

import datetime

def valid(lst, var, msg):
    valid = False
    while valid != True:
        for key in lst:
            if key == var:
                valid = True
        if valid == False: 
            var = input(msg)
            var = var.upper()
    return var
def userInput(taxes):
    bill = float(input("What is the cost of your bill?"))
    state = input("Which state are you in? Please spell out the whole state(non-abbreviated).")
    state = state.upper()
    state = valid(taxes, state, "Invalid: Please enter another state(non-abbreviated).")
    restaurant = input("Which restaurant are you dining in?")
    restaurant = restaurant.upper()
    service = input("Was your service poor, okay, or great?")
    service = service.upper()
    serviceLst = ["POOR", "OKAY", "GREAT"]
    service = valid(serviceLst, service, "Invalid: Please enter another service level.")
    return (bill, state, restaurant, service)



def getTaxInfo():
    handler = open("tax3.txt",'r')
    dataStr = handler.read()
    wordList = dataStr.rstrip().split("\n")
    taxes  = {}
    i = 0
    while i != 102:
        taxes[wordList[i]]= wordList[i+1]
        i += 2
    return taxes
        
def tax(st, b, taxInfo):   
    tax = 0
    if st in taxInfo:
        for key in taxInfo:
            if st == key:
                tax = float(taxInfo[key])
    finaltax = tax * b
    return (finaltax)            
                
def tip(s, b):
  tip = 0
  if s == "POOR":
    tip = 0.10 * b
  elif s == "OKAY":
    tip = 0.15 * b
  elif s == "GREAT":
    tip = 0.20 * b
  return tip

  
   
taxes = getTaxInfo()
bill, state, restaurant, service = userInput(taxes)
now = datetime.datetime.now().strftime('%m-%d-%Y')
t = datetime.datetime.now().strftime("%H:%M")
sigline = "X_________________"
tcost = bill

finaltax = tax(state, bill, getTaxInfo())
tcost += finaltax
tip = tip(service, tcost)
tcost += tip


finaltax = "$%.2f" %(finaltax)
tip = "$%.2f" %(tip)
bill = "$%.2f" %(bill)
tcost = "$%.2f" %(tcost)

    


def printReceipt(receipt):
    f = open("receipt.txt", "w")
    f.write("\n\n-------------------------------------------")
    f.write("\n\n")
    for key in receipt:
        if key == "SUB-TOTAL" or key == "SALES TAX" or key == "TIP" or key == "TOTAL":
            f.write("%s = %s" %(key,receipt[key]))
            f.write("\n\n")
        elif key == "DATE": 
            f.write("%s at " %(receipt[key]))
        else: 
            f.write("%s" %(receipt[key]))
            f.write("\n\n")
        
    f.write("APPROVED \nTHANK YOU FOR EATING AT " +str(restaurant)+ "!\n\n")
    f.write("--------------------------------------------\n\n")
    f.close()
receipt = {"RESTAURANT": restaurant, "STATE": state, "DATE": now,"TIME": t, "SUB-TOTAL": bill,"SALES TAX": finaltax, "TIP": tip, "TOTAL": tcost, "SIGNATURE LINE":sigline}
printReceipt(receipt)