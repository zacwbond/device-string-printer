
# Because I am an idiot and used dashes in the name...
from lib import append
import sys

text = append.append_abc(sys.argv[1])

print('****' + (text).upper().replace(' ', '_') + '****')
