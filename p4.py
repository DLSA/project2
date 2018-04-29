from __future__ import print_function
import random
import subprocess
import sys

def care():
	global 	rx1,cx1,row,column,coress,rect
	
  	for m in xrange(row-2):
  	  		for  n in xrange(column-2):
  	  				if(rect[m-1][n-1]==1 and rect[m-1][n]==1 and rect[m-1][+1]==1 and rect[m][n-1]==1 and rect[m][n]==1 and rect[m][n+1]==1 and rect[1+m][n-1]==1 and rect[m+1][n]==1 and rect[m+1][n+1]==1 ):
  	  						matrix[m][n]=1
  	  					
  	  						
	
	
T = int(raw_input());
for a in xrange(T):
	
	  row=1
	  column=1
	  flag=0
	  A = readline_int()         # reads 3 into a
	 # A=int(raw_input())
 	  printline 500 500 to stdout  # sends out cell 10 10 to prepare
 	#  print(500,"",500)
 	  
  	  flush stdout
	  x, y = readline_two_int()  # does not flush stdout; hangs on the judge
	  #x,y=raw_input().split()
	  #x=int(x)
	  #y=int(y)
	  while(row*column<=A):
	  	if(row<999 and flag==0):
	  		row=row+1
	  		flag=1
	  	elif(column<999 and flag==1 ):
	  		column=column+1
	  		flag=0
	  	else:
	  		flag=-1
  	  rx1=x
  	  rx2=x
  	  cx1=y
  	  cx2=y
  	  i=0
  	  while(i<row-2):
  	  	if(rx1>=2):
  	  		rx1=rx1-1
  	  	elif(rx2<998):
  	  		rx2=rx2+1
  	  	i=i+1
  	  k=0
  	  while(k<column-2):
  	  	if(cx1>=2):
  	  		cx1=cx1-1
  	  	elif(cx2<998):
  	  		cx2=cx2+1
  	  	k=k+1
  	  matrix=[[0 for g in xrange(row-1)] for s in xrange (column-1)]
  	  rect=[[0 for l in xrange(row)] for w in xrange (column)]
  	  coress=0
  	  x=10,y=10
  	  while(1):
  	  	for m in xrange(row-2):
  	  		for  n in xrange(column-2):
  	  			if(matrix[m][n]==0):
				 	  printline rx1+m cx1+n to stdout  
				  	  flush stdout
				  	  #print(rx1+m,"",cx1+n)
	 			       	  x, y = readline_two_int() 
					#  x,y=raw_input().split()
	 			       	  rect[m][n]=1
	 			  	  if(x==-1 and y==-1):
	 			  	  	exit
	 			  	  if(coress==1):
	 			  	  	matrix[m][n]==1
	 			  	  if(x==0 and y==0):
	 			  	  	break
	 			  	  
	 	#	if(m%30==0):
	 	#		care()
	 	
	 		 if(x==0 and y==0):
	 			  	  	break
	 			  	  	
	 	if(x==0 and y==0):
	 			  	  	break
	 			  	  		
	 			  	  
	 			  	  
	 			       	  
				   	  				
  	  			
  	  
  	  
  	  
  	  	
	  	
	  
	  


	
