#!/usr/bin/python

filename     = "data/GeoIPASNum2.csv"

from redis import Redis
# r = Redis("localhost")
r = Redis("172.16.101.102")

count = 0

for line in open(filename):

	try:
		x = line.strip().split(",")
	except:
		pass
	
	if len(x) < 3 :
		continue

	if x[0] == "startIpNum" :
		continue
	
	for i in range(len(x)) :
		if i < 3 :
			x[i] = x[i].replace("\"", "")
		else :
			x.pop()

	(num_start, num_end, as_num) = x

	key = as_num + ":" + str(count)

	r.zadd("asip", key + ":s", num_start)
	r.zadd("asip", key + ":e", num_end)

	count = count + 1
	if count % 1000 == 0 :
		print "Imported %8d" % count

print "Done %d ASNum imported" % count
