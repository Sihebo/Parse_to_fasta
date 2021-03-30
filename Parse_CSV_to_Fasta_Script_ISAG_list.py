import csv
import re

with open("ISAG_Canine_SNP_Parentage_Panels_2020.csv") as ISAG_file:
    has_header = csv.Sniffer().has_header(ISAG_file.read(1024)) # Csv Sniffer module to deduce header
    ISAG_file.seek(0)
    readCSV = csv.reader(ISAG_file, delimiter=",")
    if has_header:
        next(readCSV) # Skip header row

    list_header = []
    list_seq = []

    for row in readCSV:
        name = row[1]
        position = row[0]
        sequence = row[5]
        #sequence1 = sequence.replace("]", "")
        reg_pattern1 = "/(A|T|G|C)]"
        sequence1 = re.sub(reg_pattern1, "", sequence)
        sequence1= sequence1.replace("[", "")
        #print(sequence1)
        reg_pattern2 = "\[(A|T|G|C)/"
        sequence2 = re.sub(reg_pattern2, "", sequence)
        sequence2 = sequence2.replace("]", "")
        #print(sequence2)
        header1 = name + "_1" + ";" + position
        header2 = name + "_2" + ";" + position
        #print(header1)
            
        list_header.append(header1)
        list_header.append(header2)
           
        
        list_seq.append(sequence1)
        list_seq.append(sequence2)

print(len(list_seq))            

ISAG_fsa = open("ISAG_fsa.fasta", "w")
for i in range(len(list_seq)):
    ISAG_fsa.write(">" + list_header[i] + "\n" + list_seq[i] + "\n") 

ISAG_fsa.close()
        
        
        
    
