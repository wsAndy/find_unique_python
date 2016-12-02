#-*-coding:utf-8-*-

# in the following codes, pro means problems, base means a copy

part_pro = open("900_again.txt")
all_pro = open("all_again.txt")

base_part_pro = open("900_again.txt")


output_file = open("left_problem.txt",'w')
test_file = open("debug_all.txt",'w')
test_file2 = open("debug_900.txt",'w')

line = all_pro.readline();  #all_pro的每一行

line_part_debug = base_part_pro.readline() #这个是看题目又多少题

part_pro_line = part_pro.read() #
count = 0

show_line = 1

while True:

	if not line_part_debug:
		break
	if ord(line_part_debug[0])>=48 and ord(line_part_debug[0])<=57:

		start = 1;
		while True:
			if (ord(line_part_debug[start])>=48 and ord(line_part_debug[start])<=57):
				start = start +1
			else:
				break

		title = line_part_debug[start:len(line_part_debug)]
		test_file2.write(title)
	
	#print 'here'
	line_part_debug = base_part_pro.readline()


show_line = 1
count = 0

while True:

	if not line:
		break
	if ord(line[0])>=48 and ord(line[0])<=57:

		start = 1;
		while True:
			if (ord(line[start])>=48 and ord(line[start])<=57):
				start = start +1
			else:
				break

		title = line[start:len(line)]
		test_file.write(title)

		# print title
		index = part_pro_line.find(title);
		if index == -1:
			count = count + 1
			#说明这个题目不存在
			while True:
				output_file.write(line)
				line = all_pro.readline()

				if not line:
					break
				if ord(line[0]) >= 65 and ord(line[0]) <= 90:
					continue
				else:
					break
		else:
			line = all_pro.readline()
	else:
		line = all_pro.readline()
		
		

part_pro.close()
all_pro.close()
output_file.close()

test_file.close()
test_file2.close()

print count # 全部的不重复的题目数量
