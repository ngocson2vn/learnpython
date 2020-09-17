def binary_search(ordered_list, item):
  start_index = 0
  end_index = len(ordered_list) - 1
  while start_index <= end_index:
    mid_index = (start_index + end_index) // 2
    if ordered_list[mid_index] == item:
      return mid_index

    if ordered_list[mid_index] < item:
      start_index = mid_index + 1
    else:
      end_index = mid_index - 1
  return -1

def test():
  ordered_list = [10, 30, 100, 120, 500]
  index = binary_search(ordered_list, 100)
  print("index = {}\nordered_list[{}] = {}".format(index, index, ordered_list[index]))

if __name__ == "__main__":
  test()