#search if a string is of form 172.16.114.236
def isIpAddress(text):		#how to define a function
	if len(text)!=14:  #notice the colon
		return False  #case sensitive 
	for i in range(0,3):
		if not text[i].isdigit():
			return False  #no semi-colon at the end of statement;indentation is important 
	if text[3]!='.':
		return False
	for i in range(4,6):
		if not text[i].isdigit():
			return False
	if text[6]!='.':
		return False
	for i in range(7,10):
		if not text[i].isdigit():
			return False
	if text[10]!='.':
		return False
	for i in range(11,14):
		if not text[i].isdigit():
			return False
	return True

# note : // is not used for comments 
x=False
msg='hey my squid is running on 1723.16.114.236 and iitg server is q202.14.180.124';
for i in range(0,len(msg)):
	if(isIpAddress(msg[i:i+14])):				#how to do slicing i.e. to extract a substring using indices
		if(i!=0 and msg[i-1]==' '):
			if((i+14>=len(msg))or((not i+14>=len(msg) )and msg[i+14]==' ')):
				print("ip address found:"+msg[i:i+14])		#string concatenation 
				x=True;	#true/TRUE doesnt work 
if not x:
	print("no ip address found")
