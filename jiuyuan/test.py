import test_shenpi,sys,time,CONFIG
obj=test_shenpi.test_shenpi()
#3 safeadmin tmanager g1manager dingjia scutech
i = len(CONFIG.suser)
print i
n = len(CONFIG.operator) # ji ceng shen pi
print n
print 'kk'
while True:
	j = 0
	while j < i - 1 :
		m = 0
		while m < n - 1:
			suser = CONFIG.suser[j]
			print suser
			spassword = CONFIG.spassword[j]
			print spassword
			obj.login(suser,spassword)
			operator = CONFIG.operator[m]
			obj.approval(operator)
			m +=1
		j +=1
	time.sleep(5)