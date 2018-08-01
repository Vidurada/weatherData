import os

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


with open('flnfmas2!0519!1950!2016.raw') as f:
    file = f.readlines()
#for i in lines:
    line_num = file_len('flnfmas2!0519!1950!2016.raw')
    print(line_num)
    temp = [line[:-1] for line in file]
    #print (temp)
    for i in range (0,line_num-4,4):
        #f = open("interim_results.txt", "a+")
        single_line = temp[i]+temp[i+1]+temp[i+2]+temp[i+3]+"\n"


        #f.write(single_line+ "\n")
        #f.close()
        #print(single_line)

