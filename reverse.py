sentinel = '###'
text = input()
n= []
while text != sentinel:
	n.append(text)
	text = input()
y = n[-1::-1]
for i in y:
	print(i)

			
	
	
