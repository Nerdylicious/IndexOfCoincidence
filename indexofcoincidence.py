import re
pattern = re.compile(r"\s+")

f = open("cmystery2.txt", "r")

ciphertext = ""

for line in f:
	ciphertext += line

ciphertext = re.sub(pattern, "", ciphertext)
ciphertext = re.sub(",", "", ciphertext)
ciphertext = re.sub("-", "", ciphertext)


print "\nCiphertext:\n%s\n" % ciphertext

margin = 0.01
IC_lowerbound = 0.065 - margin
IC_upperbound = 0.065 + margin

found_m = False
stop = False
m = 0

while ((stop == False) and (found_m == False)):	
	m = m + 1
	found_m = True
	subtext = ""
	for i in range(0, m):
		j = i
		while j < len(ciphertext):
			subtext += ciphertext[j:j+1]
			j = j + m
		print "Subtext for m=%d: %s " % (m, subtext)

		#find frequency of all letters in subtext		
		frequency = {}
		for s in subtext:
			frequency[s] = frequency.get(s, 0) + 1
		
		numerator = 0
		for key, value in frequency.iteritems():
			numerator += value*(value-1)
		n = len(subtext)
		
		if n == 1:
			stop = True
			print "IC is undefined\n"
		else:
			#calculate IC
			IC = (float(numerator)) / (n*(n-1))
			print "IC = %.3f\n" % IC	

			#check if we found m
			if ((IC > IC_upperbound) or (IC < IC_lowerbound)): 		
				found_m = False
			subtext = ""

if found_m == True:
	print "m is %d\n" % m
else:
	print "m not found\nIt is likely that the ciphertext was not produced by using a substition cipher\n"
