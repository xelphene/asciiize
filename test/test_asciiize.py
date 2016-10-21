
import sys
#import asciiize
from asciiize import *

data = open(sys.argv[1]).read()
data = sanitize_multiline(data)
sys.stdout.write( data)

