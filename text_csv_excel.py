import csv


f = open('rawtext.txt', 'r')
all_at_once = f.read()
one_line_at_a_time = f.readline()
all_lines_delimited = f.readlines()


writing = open('file_to_write.txt', 'w')
writing.write('Hello World')
writing.close()