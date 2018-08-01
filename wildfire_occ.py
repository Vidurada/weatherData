import os
import xlwt

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
    n = 1
    wb = xlwt.Workbook()

    ws = wb.add_sheet("Wildfire Data")
    for i in range (0,line_num-4,4):
        #f = open("interim_results.txt", "a+")
        single_line = temp[i]+temp[i+1]+temp[i+2]+temp[i+3]+"\n"


        fs_region =  single_line[0:2]
        fs_unit =  single_line[2:4]
        fire_number = single_line[4:7]
        destrict_number = single_line[7:9]

        stat_cause = single_line[10]
        gen_cause = single_line[11]
        spesific_cause = single_line[11:13]
        class_of_people = single_line[13]

        #fire_number = i[9:13]

        ws.write(n, 0, fs_region)
        ws.write(n, 1,  fs_unit)
        ws.write(n, 2, fire_number)
        ws.write(n, 4, destrict_number)
        ws.write(n, 5, stat_cause)
        ws.write(n, 6, gen_cause)
        ws.write(n, 7, spesific_cause)
        ws.write(n, 8, class_of_people)


        #f.write(single_line+ "\n")
        #f.close()
        #print(single_line)

        n = n + 1

wb.save("formated_data3.xls")