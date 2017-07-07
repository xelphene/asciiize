
replacement_table_text = '''
e2,80,93   -   UTF-8 hyphen
e2,80,9c   "   UTF-8 curly double open quote
e2,80,9d   "   UTF-8 curly double close quote
91         '   CP1252 curly single quote
92         '   CP1252 curly single quote
93         "   CP1252 curly double quote
94         "   CP1252 curly double quote
96         -   CP1252 hyphen
97         -   CP1252 hyphen
85         ... CP1252 elipsis
c3,a1      a   UTF-8 a-acute
c3,81      A   UTF-8 A-acute
c3,a9      e   UTF-8 e-acute
c3,89      E   UTF-8 E-acute
c3,ad      i   UTF-8 i-acute
c3,8d      I   UTF-8 I-acute
c3,b3      o   UTF-8 o-acute
c3,93      O   UTF-8 O-acute
c3,ba      u   UTF-8 u-acute
c3,9a      U   UTF-8 U-acute
c3,bd      y   UTF-8 y-acute
c3,9d      Y   UTF-8 Y-acute
c3,a2      a   UTF-8 a-circumflex
c3,82      A   UTF-8 A-circumflex
c3,aa      e   UTF-8 e-circumflex
c3,8a      E   UTF-8 E-circumflex
c3,ae      i   UTF-8 i-circumflex
c3,8e      I   UTF-8 I-circumflex
c3,b4      o   UTF-8 o-circumflex
c3,94      O   UTF-8 O-circumflex
c3,bb      u   UTF-8 u-circumflex
c3,9b      U   UTF-8 U-circumflex
c3,a4      a   UTF-8 a-umlaut
c3,84      A   UTF-8 A-umlaut
c3,ab      e   UTF-8 e-umlaut
c3,8b      E   UTF-8 E-umlaut
c3,af      i   UTF-8 i-umlaut
c3,8f      I   UTF-8 I-umlaut
c3,b6      o   UTF-8 o-umlaut
c3,96      O   UTF-8 O-umlaut
c3,bc      u   UTF-8 u-umlaut
c3,9c      U   UTF-8 U-umlaut
c3,a0      a   UTF-8 a-grave
c3,80      A   UTF-8 A-grave
c3,a8      e   UTF-8 e-grave
c3,88      E   UTF-8 E-grave
c3,ac      i   UTF-8 i-grave
c3,8c      I   UTF-8 I-grave
c3,b2      o   UTF-8 o-grave
c3,92      O   UTF-8 O-grave
c3,b9      u   UTF-8 u-grave
c3,99      U   UTF-8 U-grave
c3,a3      a   UTF-8 a-tilde
c3,83      A   UTF-8 A-tilde
c3,b1      n   UTF-8 n-tilde
c3,91      N   UTF-8 N-tilde
c3,b5      o   UTF-8 o-tilde
c3,95      O   UTF-8 O-tilde
c3,a7      c   UTF-8 c-cedilla
c3,87      C   UTF-8 C-cedilla
c3,80      A   UTF-8 A-GRAVE
c3,81      A   UTF-8 A-ACUTE
c3,82      A   UTF-8 A-CIRCUMFLEX
c3,83      A   UTF-8 A-TILDE
c3,84      A   UTF-8 A-DIAERESIS
c3,85      A   UTF-8 A-RING ABOVE
c3,87      C   UTF-8 C-CEDILLA
c3,88      E   UTF-8 E-GRAVE
c3,89      E   UTF-8 E-ACUTE
c3,8a      E   UTF-8 E-CIRCUMFLEX
c3,8b      E   UTF-8 E-DIAERESIS
c3,8c      I   UTF-8 I-GRAVE
c3,8d      I   UTF-8 I-ACUTE
c3,8e      I   UTF-8 I-CIRCUMFLEX
c3,8f      I   UTF-8 I-DIAERESIS
c3,90      D   UTF-8 ETH
c3,91      N   UTF-8 N-TILDE
c3,92      O   UTF-8 O-GRAVE
c3,93      O   UTF-8 O-ACUTE
c3,94      O   UTF-8 O-CIRCUMFLEX
c3,95      O   UTF-8 O-TILDE
c3,96      O   UTF-8 O-DIAERESIS
c3,98      O   UTF-8 O-STROKE
c3,99      U   UTF-8 U-GRAVE
c3,9a      U   UTF-8 U-ACUTE
c3,9b      U   UTF-8 U-CIRCUMFLEX
c3,9c      U   UTF-8 U-DIAERESIS
c3,9d      Y   UTF-8 Y-ACUTE
c3,a0      a   UTF-8 A-GRAVE
c3,a1      a   UTF-8 A-ACUTE
c3,a2      a   UTF-8 A-CIRCUMFLEX
c3,a3      a   UTF-8 A-TILDE
c3,a4      a   UTF-8 A-DIAERESIS
c3,a5      a   UTF-8 A-RING ABOVE
c3,a7      c   UTF-8 C-CEDILLA
c3,a8      e   UTF-8 E-GRAVE
c3,a9      e   UTF-8 E-ACUTE
c3,aa      e   UTF-8 E-CIRCUMFLEX
c3,ab      e   UTF-8 E-DIAERESIS
c3,ac      i   UTF-8 I-GRAVE
c3,ad      i   UTF-8 I-ACUTE
c3,ae      i   UTF-8 I-CIRCUMFLEX
c3,af      i   UTF-8 I-DIAERESIS
c3,b1      n   UTF-8 N-TILDE
c3,b2      o   UTF-8 O-GRAVE
c3,b3      o   UTF-8 O-ACUTE
c3,b4      o   UTF-8 O-CIRCUMFLEX
c3,b5      o   UTF-8 O-TILDE
c3,b6      o   UTF-8 O-DIAERESIS
c3,b8      o   UTF-8 O-STROKE
c3,b9      u   UTF-8 U-GRAVE
c3,ba      u   UTF-8 U-ACUTE
c3,bb      u   UTF-8 U-CIRCUMFLEX
c3,bc      u   UTF-8 U-DIAERESIS
c3,bd      y   UTF-8 Y-ACUTE
c3,bf      y   UTF-8 Y-DIAERESIS
'''

def parse_replacement_table(text):
	replacement_table = []
	for line in text.split('\n'):
		if line.startswith('#'):
			continue
		parts = line.split(' ')
		parts = filter( lambda p: p!='', parts ) # remove empty strings
		if parts==[]:
			continue
		
		
		byteseq = parts[0].split(',')
		byteseq = '\\x'.join(byteseq)
		byteseq = '\\x' + byteseq
		byteseq = byteseq.decode('string_escape')
		
		repchar = parts[1]
		
		replacement_table.append((byteseq, repchar))
	return replacement_table

replacement_table = parse_replacement_table(replacement_table_text)
	
