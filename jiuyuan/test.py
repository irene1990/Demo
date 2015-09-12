import test_shenpi,sys
obj=test_shenpi.test_shenpi()
3 safeadmin tmanager g1manager dingjia scutech
num = len(sys.argv)
i = sys.argv[0] # ji ceng shen pi
j = 1
while j < i+1:
    approvalor = sys.argv[j+1]
    obj.login(approvalor,'1234')  # shen pi yuan deng lu
	m = 1
	while m < num - sys.argv[0]:#bian li cao zuo yuan
	    loginusr = sys.argv[i+1+m]
		obj.approval(loginuser)
	obj.logout()