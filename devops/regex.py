cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
...: Rostam Batmanglij <rostam@vpwk.com>,
...: Chris Tomson <ctomson@vpwk.com,
...: Bobbi Baio <bbaio@vpwk.com'''

import re
m = re.search(r'\w+@\w+\.\w+', cc_list)
print(m.group())
print("")

m2 = re.search(r'(\w+)@(\w+\.\w+)', cc_list)
print(f"Email: {m2.group(0)}")
print(f"Name: {m2.group(1)}")
print(f"Domain: {m2.group(2)}")
