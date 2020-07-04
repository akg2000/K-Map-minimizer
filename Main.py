# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Aman Kumar Gupta
# Roll Number: 2018217
# Section: B
# Group: 2
# Date: 19-10-2018

def minFunc(num, stringIn):
	epic=[]
	mc,dc=stringIn.split()
	mc=mc.replace(')',"")#slicing the given string
	mc=mc.replace('(','')
	mc=list(map(str,mc.split(',')))
	dc=dc.replace('(','')
	dc=dc.replace(')',"")
	dc=dc.replace('d','')
	dc=list(map(str,dc.split(',')))
	pi={}#creating empty dictionaries for using them afterwards
	g01={}
	g12={}
	g23={}
	g34={}
	g0112={}
	g1223={}
	g2334={}
	g01121223={}
	g12232334={}
	g0112122312232334={}
						#creating dictionaries so that we can directly assign binary values to the numbers
	dct4={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','10':'1010','11':'1011','12':'1100','13':'1101','14':'1110','15':'1111'}
	dct3={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101','6':'110','7':'111'}
	dct2={'0':'00','1':'01','2':'10','3':'11'}
	#joining the minterms and dont care in order to give us the biggest subset
	fn=mc+dc
	fn.sort()
	g0={}
	fd={}
	g1={}
	g2={}
	g3={}
	g4={}
			#the function below converts the binary even in dash format to the respective variable format
	def answer(list,n):
		empty=''
		for i in list:
			for p in range(n):
				if i[p]=='-':
					empty=empty
				else:
					if p==0:
						if i[p]=='0':
							empty=empty+'a\''
						if i[p]=='1':
							empty=empty+'a'
					if p==1:
						if i[p]=='0':
							empty=empty+'b\''
						if i[p]=='1':
							empty=empty + 'b'
					if p==2:
						if i[p]=='0':
							empty=empty+'c\''
						if i[p]=='1':
							empty=empty+'c'
					if p==3:
						if i[p]=='0':
							empty=empty+'d\''
						if i[p]=='1':
							empty=empty+'d'
			empty+=' + '
		if empty==' + ':
			return ('1')
		else:		
			return empty[:-3]
			#the function below works recursively, recursively so as to find the biggest subset and not find multiple groups already combined into upper groups to be added into the list 
	def finding_function(group,minterm_function):
		epi=[]
		if len(minterm_function)!=0:
			group=duplicate_remove(group)
			for i in minterm_function:
				for j in group:
					if j.find(i)!=-1:
						uiui=group[j]
						epi.append(uiui)
						#epi.append(j)
						epic.extend(epi)
						minterm_function.remove(i)
						if len(minterm_function)!=0:
							return (finding_function(group,minterm_function))
		else:
			epi=list(set(epi))
			return (epi)
		#this function below helps in removing duplicate elements in the dictionary , because of the logic implemented the dictionary might have duplicate elements
	def duplicate_remove(g):
		ans = {}

		for key,value in g.items():
			if value not in ans.values():
				ans[key] = value
		return(ans)
		#the 3 functions below not only combines the binary according to the number of 1's but also adds them to dictionary acording to the number of ones
	def grouper4(fn):
		for x in fn:
			if(x=='0'):
				g0[x] = dct4[x]
			if(x=='1' or x=='8' or x=='4' or x=='2'):
				g1[x] = dct4[x]
			if(x=='3' or x=='5' or x=='6' or x=='9' or x=='10' or x=='12'):
				g2[x] = dct4[x]
			if(x=='7' or x=='11' or x=='13' or x=='14'):
				g3[x] = dct4[x]
			if(x=='15'):
				g4[x] = dct4[x]
	def grouper3(fn):
		for x in fn:
			if(x=='0'):
				g0[x] = dct3[x]
			if(x=='1' or x=='4' or x=='2'):
				g1[x] = dct3[x]
			if(x=='3' or x=='5' or x=='6'):
				g2[x] = dct3[x]
			if(x=='7'):
				g3[x] = dct3[x]
	def grouper2(fn):
		for x in fn:
			if(x=='0'):
				g0[x] = dct2[x]
			if(x=='1' or x=='2'):
				g1[x] = dct2[x]
			if(x=='3'):
				g2[x] = dct2[x]
		#the below function compares any binary numbers with same number of digits
	def bitwise_compare(a,b,n):
		count=0
		null=''
		for p in range(0,n):
			if a[p]!=b[p]:
				count=count+1
				null=null+'-'
			if a[p]==b[p]:
				null=null+a[p]
		if count==1:
			return True,null
		else :
			return False,null
		# the functon below adds one dictionary to another
	def merge(dict1, dict2): 
	    return (dict2.update(dict1))
	    #conversion of integers in the dictionary caused them to have extra zeroes or an extra b when used the bin function to remove the b i made this function
	def removeb(s,n):
		a=s.find('b')
		s=s[:a] + s[a+1:]
		l=len(s)
		return (s[-n:])
		#for 4 variables
	if num=='4':
		grouper4(fn)
		merge(g3,fd);merge(g4,fd);merge(g2,fd);merge(g1,fd);merge(g0,fd)
		#now we compare bitwise from one grop to the next group in the same category and then each one from a category to the next category till 16 one is achieved
		for i in g1:
			for j in g2:
				a,b=bitwise_compare(g1[i],g2[j],4)
				if a==True:
					x=i + '&' + j
					g12[x]=b
		for i in g0:
			for j in g1:
				a,b=bitwise_compare(g0[i],g1[j],4)
				if a==True:
					x=i + '&' + j
					g01[x]=b
		for i in g2:
			for j in g3:
				a,b=bitwise_compare(g2[i],g3[j],4)
				if a==True:
					x=i + '&' + j
					g23[x]=b
		for i in g3:
			for j in g4:
				a,b=bitwise_compare(g3[i],g4[j],4)
				if a==True:
					x=i + '&' + j
					g34[x]=b
		for i in g01:
			for j in g12:
				a,b=bitwise_compare(g01[i],g12[j],4)
				if a==True:
					x=i + '&' + j
					g0112[x]=b
		for i in g12:
			for j in g23:
				a,b=bitwise_compare(g12[i],g23[j],4)
				if a==True:
					x=i + '&' + j
					g1223[x]=b
		for i in g23:
			for j in g34:
				a,b=bitwise_compare(g23[i],g34[j],4)
				if a==True:
					x=i + '&' + j
					g2334[x]=b
		for i in g0112:
			for j in g1223:
				a,b=bitwise_compare(g0112[i],g1223[j],4)
				if a==True:
					x=i + '&' + j
					g01121223[x]=b
		for i in g1223:
			for j in g2334:
				a,b=bitwise_compare(g1223[i],g2334[j],4)
				if a==True:
					x=i + '&' + j
					g12232334[x]=b
		for i in g01121223:
			for j in g12232334:
				a,b=bitwise_compare(g01121223[i],g12232334[j],4)
				if a==True:
					x=i + '&' + j
					g0112122312232334[x]=b
		#starting from the highest group we filter down to the smaller groups and kepps deleting them from the list to avoid tkaing smaller group which have already been repeated before in the bigger group
		if len(mc)!=0:
			x1=finding_function(g0112122312232334,mc)
		else:
			x1=0
		if len(mc)!=0:
			x2=finding_function(g12232334,mc)
		else:
			x2=0
		if len(mc)!=0:
			x3=finding_function(g01121223,mc)
		else:
			x3=0
		if len(mc)!=0:
			x4=finding_function(g2334,mc)
		else:
			x4=0
		if len(mc)!=0:
			x5=finding_function(g1223,mc)
		else:
			x5=0
		if len(mc)!=0:
			x6=finding_function(g0112,mc)
		else:
			x6=0
		if len(mc)!=0:
			x7=finding_function(g01,mc)
		else:
			x7=0
		if len(mc)!=0:
			x8=finding_function(g12,mc)
		else:
			x8=0
		if len(mc)!=0:
			x9=finding_function(g23,mc)
		else:
			x9=0
		if len(mc)!=0:
			x10=finding_function(g34,mc)
		else:
			x10=0
		if len(mc)!=0:
			x11=finding_function(g0,mc)
		else:
			x11=0
		if len(mc)!=0:
			x12=finding_function(g1,mc)
		else:
			x12=0
		if len(mc)!=0:
			x13=finding_function(g2,mc)
		else:
			x13=0
		if len(mc)!=0:
			x14=finding_function(g3,mc)
		else:
			x14=0
		if len(mc)!=0:
			x15=finding_function(g4,mc)
		else:
			x15=0
		#now if any minterms did not combine then it will not lie in all the above groups so it is necesaary to add those elements in the essential prime implicant list
		if x1==None and x2==None and x3==None and x4==None and x5==None and x6==None and x7==None and x8==None and x9==None and x10==None and x11==None and x12==None and x13==None and x14==None and x15==None:
			for i in mc:
				k=bin(int(i))
				gigi=(removeb(k,2))
				epic.append(gigi)
		epic=list(set(epic))#if still there is any element repeating it will filter it out
		return (answer(epic,4))
	if num=='3':
		grouper3(fn)#we group the numbers according to the number of 1's in them and then add them into the dictionary
		merge(g3,fd);merge(g2,fd);merge(g1,fd);merge(g0,fd)
		for i in g0:#from this step we repeat like with 4 variables we comapre each group with its sucessor in the category and the each group with its next category in order to find the biggest group possible
			for j in g1:
				a,b=bitwise_compare(g0[i],g1[j],3)#we compare bitwise at each step and club them together
				if a==True:
					x=i + '&' + j
					g01[x]=b
		for i in g1:
			for j in g2:
				a,b=bitwise_compare(g1[i],g2[j],3)
				if a==True:
					x=i + '&' + j
					g12[x]=b
		for i in g2:
			for j in g3:
				a,b=bitwise_compare(g2[i],g3[j],3)
				if a==True:
					x=i + '&' + j
					g23[x]=b
		for i in g01:
			for j in g12:
				a,b=bitwise_compare(g01[i],g12[j],3)
				if a==True:
					x=i + '&' + j
					g0112[x]=b
		for i in g12:
			for j in g23:
				a,b=bitwise_compare(g12[i],g23[j],3)
				if a==True:
					x=i + '&' + j
					g1223[x]=b
		for i in g0112:
			for j in g1223:
				a,b=bitwise_compare(g0112[i],g1223[j],3)
				if a==True:
					x=i + '&' + j
					g01121223[x]=b
		if len(mc)!=0:#we perform this operation in order to avoid the smaller group being appeneded into the list which have already been combined in bigger groups
			x1=finding_function(g01121223,mc)
		else:
			x1=0
		if len(mc)!=0:
			x2=finding_function(g0112,mc)
		else:
			x2=0
		if len(mc)!=0:
			x3=finding_function(g1223,mc)
		else:
			x3=0
		if len(mc)!=0:
			x4=finding_function(g01,mc)
		else:
			x4=0
		if len(mc)!=0:
			x5=finding_function(g12,mc)
		else:
			x5=0
		if len(mc)!=0:
			x6=finding_function(g23,mc)
		else:
			x6=0
		if len(mc)!=0:
			x7=finding_function(g0,mc)
		else:
			x7=0
		if len(mc)!=0:
			x8=finding_function(g1,mc)
		else:
			x8=0
		if len(mc)!=0:
			x9=finding_function(g2,mc)
		else:
			x9=0
		if len(mc)!=0:
			x10=finding_function(g3,mc)
		else:
			x10=0 #we did this in order to see that if any minterm didnot combnie with anyother minterm then it mst be added to the essential prime implicant list
		if x1==None and x2==None and x3==None and x4==None and x5==None and x6==None and x7==None and x8==None and x9==None and x10==None:
			for i in mc:
				k=bin(int(i))
				gigi=(removeb(k,2))
				epic.append(gigi)
		epic=list(set(epic))
		return (answer(epic,3))
	if num=='2':
		grouper2(fn)#we group the binaries according to the number of 1's in them while adding them to seperate dictionaries
		merge(g2,fd);merge(g1,fd);merge(g0,fd)
		for i in g0:#we comapre each group bitwise with the next group in its categpry and then repead the same with all categories , to reach the biggest category of 4
			for j in g1:
				a,b=bitwise_compare(g0[i],g1[j],2)
				if a==True:
					x=i + '&' + j
					g01[x]=b
		for i in g1:
			for j in g2:
				a,b=bitwise_compare(g1[i],g2[j],2)
				if a==True:
					x=i + '&' + j
					g12[x]=b
		for i in g01:
			for j in g12:
				a,b=bitwise_compare(g01[i],g12[j],2)
				if a==True:
					x=i + '&' + j
					g0112[x]=b
		if len(mc)!=0:#this is done to avoid of same minterms coming as part of smaller and bigger groups in different categories
			x=finding_function(g0112,mc)
		else:
			x=0
		if len(mc)!=0:
			x2=finding_function(g01,mc)
		else:
			x2=0
		if len(mc)!=0:
			x3=finding_function(g12,mc)
		else:
			x3=0	
			#this is done if someminterm does not combine with any other minterm then it must be added to the essential prime implicant list in order to find the answer
		if x==None and x2==None and x3==None:
			for i in mc:
				k=bin(int(i))
				gigi=(removeb(k,2))
				epic.append(gigi)
		epic=list(set(epic))
		return (answer(epic,2))
