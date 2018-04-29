import sys
T = int(raw_input());C
i=0
k=0
t=len(array)
while(array[t-1]==1):
	t=t-1
def recur(a,arr):
		global k
		global t
		print a
		if(a>=t-1):
			k=k+1
			return;
		if(a+1<t):
			if(arr[a+1]!=1):
				recur(a+1,arr)
		if(a+2<t):
			if(arr[a+2]!=1 ):
				recur(a+2,arr)
		if(a+3<t):
			if(arr[a+3]!=1 ):
				recur(a+3,arr)

		return
m=0

while(array[m]!=0 and m< len(array)-1):
	m=m+1
print m
if(m<=3):
	 recur(m,array)
print (k%1000000007)

		

