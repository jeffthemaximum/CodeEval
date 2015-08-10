test = 20

coin1, coin2, coin3, coin_count = 5, 3, 1, 0
bigs, mediums, smalls = 0, 0, 0

#deduct 5 coin
if test >= coin1:
	bigs = test / coin1
	coin_count = coin_count + bigs
	test = test - (bigs * coin1)

#deduct 3 coin
if test >= coin2:
	mediums = test / coin2
	coin_count = coin_count + mediums
	test = test - (mediums * coin2)

#deduct 1 coin
if test >= coin3:
	smalls = test / coin3
	coin_count = coin_count + smalls
	test = test - (smalls * coin1)

print coin_count