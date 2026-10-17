# File Handling! A small topic, but we are going to deep dive in it..

# 'sample.txt' doesn't exist yet
f = open('sample.txt', 'w')
f.write('Hello World')
f.close()

# below won't work because we closed the file
f.write('hello')

# from future (03), 03_file_present.py replaces txt content in sample.txt