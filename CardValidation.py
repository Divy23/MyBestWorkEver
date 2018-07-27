card_nbr=input("Please enter the card number: ")
mastercard_list=["51", "52","53", "54", "55"]
amex_list=["34", "37"]

#Checking Length

def card_type(card_nbr):
	if card_nbr[0]=="4" and len(card_nbr)==16:
		card_type="Visa"
	elif card_nbr[0:2] in mastercard_list and len(card_nbr)==16:
		card_type="Mastercard"
	elif card_nbr[0:2] in amex_list and len(card_nbr)==15:
		card_type="AMEX"
	elif card_nbr[0:4]=="6011" and len(card_nbr)==16:
		card_type="Discover"
	else:
		card_type="Invalid"	

	print(card_nbr[0:4], card_type)	
	return card_type


card_type(card_nbr)


my_list=[]
def valid_card(card_nbr):

	for i in range(len(card_nbr)):

		my_list.append(int(card_nbr[i]))

	print(card_nbr)
	print(my_list)

	for i in range(len(my_list)-2,-1,-2):
		print(i)
		# print(my_list[i])
		my_list[i]=int(my_list[i])*2
		print(i, my_list)
		if len(str(my_list[i]))>1:
			string=str(my_list[i])
			string=int(string[0])+int(string[1])
			my_list[i]=string
			print(string)
	print(my_list)		
	sum=0		
	for i in range(len(my_list)):
		sum += int(my_list[i])
	if sum % 10==0:
		flag="Valid Card"
	else:
		flag="Invalid Card"
	print(flag)	
	return flag	
		
	
valid_card(card_nbr)	


#Art Solution

class CreditCard:
    
    def __init__(self, card_number, valid=False):
        self.card_number = card_number
        self.card_type = self.determine_card_type()
        self.valid = valid
        self.yes = self.yesd()


#Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        m = ["51", "52", "53", "54", "55"]
        a = ["34", "37"]
        v = ["4"]
        d = ["6011"]

        if self.card_number[:2] in m:
            self.card_type = "Mastercard"
        elif self.card_number[:2] in a: 
            self.card_type = "AMEX"
        elif self.card_number[0] in v: 
            self.card_type = "Visa"
        elif self.card_number[:4] in d: 
            self.card_type = "Discover"
        else:
            self.card_type = "Not valid"
        return self.card_type



#Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if self.card_type == "Not valid": # IF check to make sure that if the len(self.card_number) is correct, but type is unknown
            print("Not a valid card type. Discard length")
        elif len(self.card_number) == 16:
            print("It's got to be a VISA or MC")
        elif len(self.card_number) == 15:
            print("It's got to be an AMEX")
        else:
            print("Not a credit card")
    
# #Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        if self.card_type != "Not valid": # Must add check here to avoid calculatng mod%10 if card not any of above types
            dig = []
            all_dig = []
            num_str_reversed = self.card_number[::-1]
            even = False
            for i in num_str_reversed:
                num = int(i)
                if even:
                    num *= 2
                    dig.append(num if num < 10 else 1+num%10)
                    even = False
                else:
                    all_dig.append(num)
                    even = True
            
            check_sum = sum(dig) + sum(all_dig)

            if check_sum % 10 == 0:
                self.valid = True
            else:
                self.valid = False
            return self.valid # Must return something in order for print() in main() to display something.
        else:
            self.valid = False
            print("Unidentifiable Card number") #Display message in the case that the card is not Visa/Mastercard/AMEX/Discover
            return self.valid

    def yesd(self):
        self.yes = 'YYYYYY'
        return self.yes 

    def main(self):
        print(self.validate())



cc = CreditCard('5515460934365316')
print("Atr of card",cc.card_type)
cc.determine_card_type()
cc.check_length()
# cc.validate() # Do not need to run validate() if being invoked in main() method.
cc.main()



# #do not modify assert statements

# cc = CreditCard('9999999999999999')

# assert cc.valid == False, "Credit Card number cannot start with 9"
# assert cc.card_type == "INVALID", "99... card type is INVALID"

# cc = CreditCard('4440')

# assert cc.valid == False, "4440 is too short to be valid"
# assert cc.card_type == "INVALID", "4440 card type is INVALID"

# cc = CreditCard('5515460934365316')

# assert cc.valid == True, "Mastercard is Valid"
# assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

# cc = CreditCard('6011053711075799')

# assert cc.valid == True, "Discover Card is Valid"
# assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

# cc = CreditCard('379179199857686')

# assert cc.valid == True, "AMEX is Valid"
# assert cc.card_type == "AMEX", "card_type is AMEX"

# cc = CreditCard('4929896355493470')

# assert cc.valid == True, "Visa Card is Valid"
# assert cc.card_type == "VISA", "card_type is VISA"

# cc = CreditCard('4329876355493470')

# assert cc.valid == False, "This card does not meet mod10"
# assert cc.card_type == "INVALID", "card_type is INVALID"

# cc = CreditCard('339179199857685')

# assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
# assert cc.card_type == "INVALID", "card_type is INVALID"



Collapse 







		



