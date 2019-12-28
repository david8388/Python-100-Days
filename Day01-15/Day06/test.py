# from module1 import foo

# foo() # hello world

# from module2 import foo
# foo() # goodbye world

import module2 as m2
import module1 as m1

m1.foo()
m2.foo()