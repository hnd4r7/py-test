
"""
import modules
"""

print("-"*100)
print("current name: ", __name__)

import imp 
print(imp.foo2("aaa",aa = 'bb',cc ='dd',ee= 'ff'))
print("imp's name::::",imp.__name__)

from imp import foo2 
foo2('ccc')

def foo2(name):
    print("foo current" , name)
    global sys
    import sys

foo2('ddd')
foo2 = imp.foo2
print(sys.path)

import builtins
print(dir(builtins))


'''
from pathlib import Path

package = Path('package')
package.mkdir()

(package / '__init__.py').write_text("""
from .module_1 import *
from .module_2 import *
""")

package_module_1 = package / 'module_1.py'
package_module_1.write_text("""
__all__ = ['foo']
imp_detail1 = imp_detail2 = imp_detail3 = None
def foo(): pass
""")

package_module_2 = package / 'module_2.py'
package_module_2.write_text("""
__all__ = ['Bar']
imp_detail1 = imp_detail2 = imp_detail3 = None
class Bar: pass
""")

subpackage_1 = package / 'module_1'
subpackage_1.mkdir()
subpackage_2 = package / 'module_2'
subpackage_2.mkdir()

package_module_1.rename(subpackage_1 / 'foo_implementation.py')
package_module_2.rename(subpackage_2 / 'Bar_implementation.py')

(subpackage_1 / '__init__.py').write_text("""
from .foo_implementation import *
__all__ = ['foo']
""")
(subpackage_2 / '__init__.py').write_text("""
from .Bar_implementation import *
__all__ = ['Bar']
""")
'''

from package import * 
Bar()
Baz()
print(test)

# print(l)
from basic import *
print(l)
print(xxx) # -> basic -> cal 级联引用
print(os.name)  # -> basic -> os 级联引用
