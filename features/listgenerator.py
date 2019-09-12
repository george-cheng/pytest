# a = [m + n for m in 'ABCDEFJHIJKLMNOPQRSTUVWXYZ' for n in 'ABCDEFJHIJKLMNOPQRSTUVWXYZ']
# print(a)

import os
a = [a for d in os.listdir('.')]
print(a)