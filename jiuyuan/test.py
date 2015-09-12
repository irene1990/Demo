import test_shenpi,sys,time
obj=test_shenpi.test_shenpi()
#3 safeadmin tmanager g1manager dingjia scutech
num = len(sys.argv)
k = sys.argv[0] # ji ceng shen pi
while True:
	i = 2
	j = 1
	while j < i+1 :
		m = 0
		while m < num - i -2:
			approvalor = sys.argv[j+1]
			obj.login(approvalor,'Dingjia123!')
			loginuser = sys.argv[i+m+2]
			obj.approval(loginuser)
			m +=1
		j +=1
	time.sleep(5)