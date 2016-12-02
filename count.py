#-*-coding:utf-8-*-
# 

# left_problem.txt includes those problems that not occur in all_again.txt
# this problem could count the size of those problem

base_part_pro = open('left_problem.txt')
line_part_debug = base_part_pro.readline()


all_line = 1

while True:

	if not line_part_debug:
		break
	if ord(line_part_debug[0])>=48 and ord(line_part_debug[0])<=57:
		all_line = all_line + 1
		start = 1;

		while True:
			if (ord(line_part_debug[start])>=48 and ord(line_part_debug[start])<=57):
				start = start +1
			else:
				break
	
	#print 'here'
	line_part_debug = base_part_pro.readline()

print all_line