'''
17. Number letter counts

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
letterMap = {0:0,1:len('one'),2:len('two'),3:len('three'),4:len('four'),5:len('five'),6:len('six'),7:len('seven'),8:len('eight'),9:len('nine'),10:len('ten'),11:len('eleven'),12:len('twelve'),13:len('thirteen'),14:len('fourteen'),15:len('fifteen'),16:len('sixteen'),17:len('seventeen'),18:len('eighteen'),19:len('nineteen'),20:len('twenty'),30:len('thirty'),40:len('forty'),50:len('fifty'),60:len('sixty'),70:len('seventy'),80:len('eighty'),90:len('ninety')}

hundredLen = len('hundred')
andLen = len('and')

count = 0
for i in range(1,1001):
	if i in letterMap:
		count += letterMap[i]
	elif i/100 < 1: # tens
		count += letterMap[int(i/10)*10] # 40
		count += letterMap[i%10] # 2, 0
	elif i < 1000:
		digit3, digit2, digit1 = int(i/100), int(i/10)%10, i%10
		count += (letterMap[digit3] + hundredLen)
		count += 0 if digit2 == 0 and digit1 == 0 else andLen # no 'and' for 100
		count += letterMap[digit2*10+digit1] if digit2 == 1 else letterMap[digit2*10]+letterMap[digit1]
	else:
		count += len('one')+len('thousand')

print(count) # 21124