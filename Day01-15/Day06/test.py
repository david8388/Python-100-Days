# from module1 import foo

# foo() # hello world

# from module2 import foo
# foo() # goodbye world

import module2 as m2
import module1 as m1
import module3 as m3

m1.foo()
m2.foo()
print('call module3')
m3.foo()
m3.bar()
print('call module3 end')