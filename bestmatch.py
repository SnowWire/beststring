from collections import OrderedDict
def string(string1,string2,string3,string4,string5):
#	string1 = "test"
#	string2 = "testing"
#	string3 = "tted"
#	string4 = "sts"
	lengs = []
	counts = []
	count1 = 0
	count2 = 0
	count3 = 0
	count4 = 0
	s2 = 0
	s3 = 0
	s4 = 0
	s5 = 0
	winner = []
	lengs.append(len(string1) - len(string2))
	for i in range(min(len(string1), len(string2))):
		if string1[i] == string2[i]:
			count1 = count1 + 1

	lengs.append(len(string1) - len(string3))
	for i in range(min(len(string1), len(string3))):
		if string1[i] == string3[i]:
			count2 = count2 + 1

	lengs.append(len(string1) - len(string4))
	for i in range(min(len(string1), len(string4))):
		if string1[i] == string4[i]:
			count3 = count3 + 1
	lengs.append(len(string1) - len(string5))
	for i in range(min(len(string1), len(string5))):
		if string1[i] == string5[i]:
			count4 = count4 + 1
	counts.append(count1)
	counts.append(count2)
	counts.append(count3)
	counts.append(count4)
	mins = min(lengs, key=abs)
	if lengs[0] == mins:
		s2 += 1
	if lengs[1] == mins:
		s3 += 1
	if lengs[2] == mins:
		s4 += 1
	if lengs[3] == mins:
		s5 += 1
	max1 = max(counts, key=abs)
	if counts[0] == max1:
		s2 += 1
	if counts[1] == max1:
		s3 += 1
	if counts[2] == max1:
		s4 += 1
	if counts[3] == max1:
		s5 += 1
	winner.append(s2)
	winner.append(s3)
	winner.append(s4)
	winner.append(s5)
	max2 = max(winner)
	OrderedDict((x, True) for x in winner).keys()
	if winner[0] == max2:
		win = string2
	elif winner[1] == max2:
		win = string3
	elif winner[2] == max2:
		win = string4
	elif winner[3] == max2:
		win = string5
	return win