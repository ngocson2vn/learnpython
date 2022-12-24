#!/usr/bin/python

def find_longest_file_path(string):
	path_dir = {}
	path_max = ""
	max_len = 0
	for line in string.splitlines():
		name = line.lstrip('\t')
		depth = len(line) - len(name)

		if '.' not in name:
			path_dir[depth] = name
		else:
			absolute_path = "\\".join(path_dir.values()) + "\\" + name
			print absolute_path
			if len(absolute_path) > max_len:
				max_len = len(absolute_path)
				path_max = absolute_path
	return max_len, path_max


string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print find_longest_file_path(string)