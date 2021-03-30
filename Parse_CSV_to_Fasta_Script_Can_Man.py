import csv
import re

with open("CanineHD_B.csv") as Canine_man_file: #Open manifest CSV
    has_header = csv.Sniffer().has_header(Canine_man_file.read(1024)) # Csv Sniffer module to deduce header
    Canine_man_file.seek(0)
    readCSV = csv.reader(Canine_man_file, delimiter=",")
    if has_header:
        next(readCSV) # Skip header row
    
    list_header = [] #Create global empty list for headers
    list_seq = [] #Create global empty list for sequences

    for row in readCSV: #Looping over every row of input file
        name = row[0] #Storing SNP name from column 1 in variable
        try:
            sequence = row[16] #Storing sequence from column 16 in variable
        except IndexError:
            print("Error while parsing sequence.")
            
            
        try:
            position = row[9] + ";" + row[10] # Storing Chr and mapinfo in variable
        except IndexError:
            print("Error while parsing position.")
        #Store sequences with both possible SNP genotypes in variables
        reg_pattern1 = "/(A|T|G|C)]"
        sequence1 = re.sub(reg_pattern1, "", sequence)
        sequence1= sequence1.replace("[", "")
        
        reg_pattern2 = "\[(A|T|G|C)/"
        sequence2 = re.sub(reg_pattern2, "", sequence)
        sequence2 = sequence2.replace("]", "")
        
        header1 = name + "_1" + ";" + position
        header2 = name + "_2" + ";" + position
        
        #Append header and sequence to lists    
        list_header.append(header1)
        list_header.append(header2)
           
        
        list_seq.append(sequence1)
        list_seq.append(sequence2)

            
#Write header and sequence lists to fasta file
Can_fsa = open("Can_man_fsa.fasta", "w")
for i in range(len(list_seq)):
    Can_fsa.write(">" + list_header[i] + "\n" + list_seq[i] + "\n") 

Can_fsa.close()
        
        
        
    
