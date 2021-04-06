s="titlei"
S="smsabm"
S=list(S)
s=list(s)
nums=[]
nums1=[]
nums2=[]
for i in range(len(s)):
	if s.count(s[i])>=2:
		nums1.append(s.count(s[i]))
		nums.append(s.index(s[i]))
		b=s[i]
		s[i]=0
		for j in range(len(s)):
			if s[j]==b:
				nums.append((s.index(s[j])))

