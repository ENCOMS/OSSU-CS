# sixtieth example: importing the library, selecting only to import 1 function in this case hello

import sys

from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
