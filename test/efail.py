import sys
sys.path.append('/me/home/devel/asciiize')
import asciiize

text=open('quotefail.txt').read()

(nt,rmchars) = asciiize.sanitize_diag(text)

for rmchar in rmchars:
	print 'RMCHAR: ',repr(rmchar)

print
print nt


