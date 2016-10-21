
def main():
	accent_type = ['']
	for line in open('accent_table.txt'):
		line = line.strip()
		if line.startswith('/'):
			accent_type[0] = line[1:]
		else:
			(inchar, outchar) = line.split(' ')
			incharcodes = repr(inchar)[1:-1]
			incharcodes = incharcodes.split('\\x')[1:]
			incharcodes = ','.join(incharcodes)
			#print incharcodes,outchar,accent_type[0]
			print '%-10s %s %s' % (
				incharcodes, outchar, 
				'UTF-8 %s-%s' % (outchar, accent_type[0])
			)

if __name__ == '__main__':
	main()
