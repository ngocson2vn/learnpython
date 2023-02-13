def enough_gpu_mem_left(left_threshold=800*1024*1024):
  print("left_threshold = {}".format(left_threshold))
  remain_to_limit_threshold = 5
  if remain_to_limit_threshold > 0:
    left_threshold = remain_to_limit_threshold * 1024 * 1024 * 1024
  print("left_threshold = {}".format(left_threshold))

enough_gpu_mem_left()