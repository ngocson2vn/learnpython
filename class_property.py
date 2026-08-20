class ConfigBundle:
  _bundle_counter = 0

  def gen_name(self):
    counter = ConfigBundle._bundle_counter
    bundle_name = f"ConfigBundle_{counter}"
    print(f"bundle_name = {bundle_name}")
    ConfigBundle._bundle_counter += 1

c1 = ConfigBundle()
c1.gen_name()

c2 = ConfigBundle()
c2.gen_name()
