import sys 
def recur():
		global array,perfect,siz
		siz=len(array)
		sort=0
		perfect=1
		while(sort!=1):
				sort=1
				for i in xrange(siz-2):
					if(array[i]>array[i+2]):
						sort=0
						a=array[i+2]
						array[i+2]=array[i]
						array[i]=a
		for i in xrange(siz-1):
				if(array[i]>array[i+1]):
					perfect=0
					return i
			
			
					 
		
				
		
			
		
				
	
	
	
T = int(raw_input());
for j in xrange(T):
	perfect=0
	siz = int(raw_input());
        array = [int(x) for x in raw_input().strip().split()]
	m=recur()
	if(perfect==1):
		sys.stdout.write("Case #")
		print j+1,
		sys.stdout.write(":")
		print "","OK"
	else:
		sys.stdout.write("Case #")
		print j+1,
		sys.stdout.write(":")
		print "",m
	

	
