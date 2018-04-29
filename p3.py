import sys 
def president():
		global beam,siz,shield,reck,charge,damage,hack
		chance=-1
		for i in xrange(siz-1,0,-1):
			if(damage[i-1]==0 and damage[i]!=0):
				chance=1
				charge[i]=charge[i-1]
				charge[i-1]=0
				damage[i-1]=(charge[i])/2
				damage[i]=0
				hack=hack+1
				i=siz-1
				if(sum(damage)<=shield):
					return 1
		if(chance==-1):
			return -1
		return 0
					
T = int(raw_input());
for j in xrange(T):
		shield,beam=(raw_input().split())
		shield=int(shield)
		siz=len(beam)
		power=1
		hack=0
		damage=[0]*siz
		charge=[0]*siz
		for i in xrange(siz):
			if(beam[i]=='C'):
				power=2*power
				charge[i]=power
			else:
				damage[i]=power
		#print charge
		#print damage
		reck=int(sum(damage))
		saved=0
		#print shield,reck
		if(shield>=reck):
			sys.stdout.write("Case #")
			print j+1,
			sys.stdout.write(":")
			print "",saved 
			continue
		else:
			while(saved!=1 and saved!=-1):
					saved=president()
			if(saved==-1):
					sys.stdout.write("Case #")
					print j+1,
					sys.stdout.write(":")
					print "","IMPOSSIBLE"
			else:
					
					sys.stdout.write("Case #")
					print j+1,
					sys.stdout.write(":")
					print "",hack
					
