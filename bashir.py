
#Abubakar Bashir Muhammad
#u19/fns/csc/1071
#Computer science
#CSC 104 Assignment
#BANK USSD FOR UBA(*919#)


print("Please type in your bank USSD.")
option=input("")
print("1AirtimeSelf\n2AirtimeOthers\n3TransferUBA\n4TransferOtherBanks\n5.Transfer-UBA prepaid\n6CheckBalance\n7.Pay Bills\n8.Next")
option=input("")
if (option=="1"):
	print("Please Enter PIN:")
pin=input("")
print("Please enter amount (50-10000):")
amount=input("")
print("Comfirm Transaction.")
print("1.YES\n2.NO")
print("please Enter PIN:")
option = input("")
if (option == "1"):
	print("Transaction Succesful") 
elif (option == "2"):
	print("Transaction Canceld")
else:
	print("Wrong input")
print("0.RETURN TO MAIN MENU.	\n00.END.")
main=input("")
if(main=='0'):
	print("1.Airtime-Self\n2.AirtimeOthers\n3.Transfer-UBA\n4Transfer-Other Banks\n5.Transfer-UBA prepaid\n6.CheckBalance\n7.Pay Bills\n8.Next")
elif(main=="00"):
	print("Thank you for banking with UBA.")
else:
	print("wrong input")
	
	



