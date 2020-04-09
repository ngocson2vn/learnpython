def singleton(aClass):
  instances = {}
  def onCall(*args, **kwargs):
    if aClass.__name__ not in instances:
      instances[aClass.__name__] = aClass(*args, **kwargs)
    return instances[aClass.__name__]
  return onCall
