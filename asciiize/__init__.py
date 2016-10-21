
import sys

from asciiize.reptable import replacement_table

def sanitize_multiline(s):
	return sanitize(s, passchars=('\n','\t','\r')  )

def sanitize_oneline(s):
	return sanitize(s)

def sanitize(s, passchars=[]):

	'''given a string containing text of an unknown encoding (i.e. arbitrary
	byte sequences), munge it as best as we can to plain printable ascii. 
	Unknown characters will be removed.  Changes CP1252 and unicode curly
	quotes and dashes to their nearest ascii equivalent.  Changes accented
	characters into un-accented ones.  A string containing only printable
	ascii characters (bytes 32-126 inclusive).  Any characters in passchars
	which do not get substituted will be returned literally.  Otherwise,
	repchar will be returned in their place.'''
	
	passchars = set(passchars)

	for (searchkey, replacement) in replacement_table:
		s = s.replace(searchkey, replacement)

	ss = ''
	for c in s:
		if ord(c) >= 32 and ord(c) <= 126:
			ss += c
		elif c in passchars:
			ss += c
		else:
			pass

	return ss

