#!/usr/bin/env python

import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM" #we can change this into "upper = lower.upper",
# because the ".upper" means that you convert the lowercase letters into uppercases
symbols = ";:,.%{}()[]"
numbers = "0123456789"

all = lower + upper + symbols + numbers
length = 8
password = "".join(random.sample(all,length))
print(password)
