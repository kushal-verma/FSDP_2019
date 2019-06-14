with open('copy.py', mode='rt') as file :
      with open('copy_txt.py', mode='wt') as file_copy:
        for line in file : 
           file_copy.write(line)            