def encode(e) :
	alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
	ALPHA=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if e in alpha :
		print(alpha[alpha.index(e)+13], end='')
	elif e in ALPHA :
		print(ALPHA[ALPHA.index(e)+13], end='')	
	else:
		print(e , end='')

def decode(d) :
	alpha='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
	ALPHA='ABCDEFGHIJKLMNOPQRSTUVWXYZAPCDEFGHIJKLMNOPQRSTUVWXYZ'
	if d in alpha :
		print(alpha[alpha.find(d,2)-13], end='')
	elif d in ALPHA :
		print(ALPHA[ALPHA.find(d,2)-13], end='')	
	else:
		print(d , end='')

print("""                                                                                                   
                                                                                                  
RRRRRRRRRRRRRRRRR        OOOOOOOOO     TTTTTTTTTTTTTTTTTTTTTTT       1111111    333333333333333   
R::::::::::::::::R     OO:::::::::OO   T:::::::::::::::::::::T      1::::::1   3:::::::::::::::33 
R::::::RRRRRR:::::R  OO:::::::::::::OO T:::::::::::::::::::::T     1:::::::1   3::::::33333::::::3
RR:::::R     R:::::RO:::::::OOO:::::::OT:::::TT:::::::TT:::::T     111:::::1   3333333     3:::::3
  R::::R     R:::::RO::::::O   O::::::OTTTTTT  T:::::T  TTTTTT        1::::1               3:::::3
  R::::R     R:::::RO:::::O     O:::::O        T:::::T                1::::1               3:::::3
  R::::RRRRRR:::::R O:::::O     O:::::O        T:::::T                1::::1       33333333:::::3 
  R:::::::::::::RR  O:::::O     O:::::O        T:::::T                1::::l       3:::::::::::3  
  R::::RRRRRR:::::R O:::::O     O:::::O        T:::::T                1::::l       33333333:::::3 
  R::::R     R:::::RO:::::O     O:::::O        T:::::T                1::::l               3:::::3
  R::::R     R:::::RO:::::O     O:::::O        T:::::T                1::::l               3:::::3
  R::::R     R:::::RO::::::O   O::::::O        T:::::T                1::::l               3:::::3
RR:::::R     R:::::RO:::::::OOO:::::::O      TT:::::::TT           111::::::1113333333     3:::::3
R::::::R     R:::::R OO:::::::::::::OO       T:::::::::T           1::::::::::13::::::33333::::::3
R::::::R     R:::::R   OO:::::::::OO         T:::::::::T           1::::::::::13:::::::::::::::33 
RRRRRRRR     RRRRRRR     OOOOOOOOO           TTTTTTTTTTT           111111111111 333333333333333   
                                                                                                  
                                                                                                  
                                                                                    # Powered by: Mr. CaT                    
                                                                                                  
                                                                                                  
                                                                                                  
                                                                                                  """)

i=1
while i==1 :
	print('1:Encrypt\n2:Decrypt\n')
	decision=input('What do you need? --> ')
	if decision == '1' :
		word=input('Enter the message to Encrypt --> ')
		for e in word :
			encode(f"{e}")
		print('\n')	
	elif decision == '2' :
		word=input('Enter a message to Decrypt --> ')
		for d in word :
			decode(f"{d}")
		print('\n')		
	else:
		print("Unrecognized Method")
	print('-----------------------------------------------------------------')	