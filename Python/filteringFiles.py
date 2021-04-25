
def parseFile(fname):
	f = open('stuff.txt','r')
	lines = f.readlines()
	dct = {}
	for line in lines:
		entry = line.split(":")
		ip = entry[0]
		town = entry[1].strip()
		dct[ip] = town
	return dct
	#print(dct)

#Input  dct is dictionary of key value pairs (ips and towns)
#       s is the string you want to filter in the IP     
def filter(dct, s):  
	lst = []
	#look through dct to find keys that match s (using find function)
	#if a match, add to lst
	for ip, town in dct.items():
		#print(ip, '->', town)
		if ip.find(s) != -1 and town not in lst:
			lst.append(town)
	return lst

def main():
	#parse the file
	dct = parseFile('stuff.txt')
	#ask user for "filter"
	s = input("what filter would you like to apply to the IP? ")
	#call filter function
	matches = filter(dct,s)
	#write all matches (towns) to console (or it could be a file)
	print(matches)


main()