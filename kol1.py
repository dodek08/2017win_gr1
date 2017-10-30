#Banking simulator. Write a code in python that simulates the banking system. 
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#!#!usr/bin/env python2.7

class Client:
	def __init__(self,params): #name
		self.name=params
		self.account=0

class Bank:
	def __init__(self,name):
		self.name=name
		self.clientslist=[]
		self.money_in=0
		self.money_out=0

	def add_client(self,newclient):
		self.clientslist=self.clientslist.append(Client(newclient))

	def cash_on_accounts(self):
		sum=0
		for i in range(len(self.clientslist)):
			sum=sum+self.clientslist[i].account
		return sum
	def client_info(self):
		if len(self.clientslist) == 0:
			print('there is no clients!')
			return 0
		else:
			for i in range(len(self.clientslist)):
				print(self.clientslist[i].name,' owns $',self.clientslist[i].account)

	def client_puts_money(self,params): #name amount
		name=params[0]
		amount=params[1]
		self.money_in=self.money_in+amount
		for i in range(len(self.clientslist)):
			if name == self.clientslist[i].name:
				self.clientslist[i].account=self.clientslist[i].account+amount
			else:
				continue

	def client_withdraws_money(self,params): #name amount
		name=params[0]
		amount=params[1]
		self.money_out=self.money_out+amount
		for i in range(len(self.clientslist)):
			if name == self.clientslist[i].name:
				self.clientslist[i].account=self.clientslist[i].account-amount
			else:
				continue

B=Bank('Test')
B.add_client('d')
B.add_client('e')
B.client_info()
B.client_puts_money(['d',100])
B.cash_on_accounts()
B.client_withdraws_money(['d',100])
# C=Client("C")
# D=Client("D")
# E=Client("E")
# clientslist=[C, D, E]
# print(clientslist[1].name)