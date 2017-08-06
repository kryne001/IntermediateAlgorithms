#
#------------------------------------------------------------------------------
# Author:      amir
# Created:     10/25/2015
#
# Instructions:
#
# 1) Make sure to rename the file (studentNetId.py) to your netId. (Do not include your first name, last name ... or any extra character)
# 2) To run the program type the following statement in the command line:  
#       -) python studentNetId.py DNASeq1FilePath DNASeq2FilePath OutputFilePath                                                                   
#    where  DNASeq1FilePath is the path to the file that contains First DNA sequence (e.g. DNASeq1.txt)
#           DNASeq2FilePath is the path to the file that contains Second DNA sequence (e.g. DNASeq2.txt)
#           OutputFilePath is the path that the output is goint to be saved (e.g. out.txt)
# 3) Make sure to replace FirstName, LastName, SectionNumber, NetId in studentInfo with your information
# 4) You may add as many functions as you want to this program
# 5) The core function in your program is DNASeqAlignment function, where it takes three arguments (DNASeq1,DNASeq2,outputPath) and 
#    computes the similarityScore, sequenceAlignment1 and sequenceAlignment2. At the end, the function writes the result to the output file (Do not make any changes to the output section).
# 6) sequenceAlignment1 and sequenceAlignment2 are strings and they are composed of following characters: 'A', 'T', 'G', 'C' and '-', Do not include extra space or any other character in the strings.
# 7) Make sure your program works with at least one of the following python versions: (2.7.9, 2.7.8, 2.6.6)
# 8) Once you have tested your program with one of the versions listed above, assign that version number to pythonVersion in studentInfo function
# 9) Make sure to write enough comments in order to make your code easy to understand. 
# 10) Describe your algorithm in ALGORITHM section below (you may add as many lines as you want).
# 11) To understand the flow of the program consider the following example:
#      0) Let say we have DNASeq1.txt file which contains AACCTGACATCTT and DNASeq2.txt file contains CCAGCGTCAACTT
#      1) If we execute the following command in the command line: -) python studentNetId.py DNASeq1.txt DNASeq2.txt out.txt
#      2) input arguments are parsed       
#      3) studentInfo() function will be executed and the output will be saved in out.txt file
#      4) DNASeqAlignment() function will be called
#      5) At the entry of the DNASeqAlignment function, DNASeq1='AACCTGACATCTT' and DNASeq2='CCAGCGTCAACTT'
#      6) You should compute the sequence alignment of DNASeq1 and DNASeq2. Let say the result is as follows:
#       A A C C T G A C - - - - A T C T T
#       | | | | | | | | | | | | | | | | |
#       - - C C A G - C G T C A A - C T T      
#      7) At the end of the DNASeqAlignment function sequenceAlignment1='AACCTGAC----ATCTT', sequenceAlignment2='--CCAG-CGTCAA-CTT', similarityScore=6.25
#      8) In the output section the result is going to be saved in out.txt file
#-------------------------------------------------------------------------------

# ALGORITHM: 
# 
#
#
#
#


import os
import sys
import argparse


def studentInfo():
    pythonVersion = 'Version'
    studentFirstName = "Kyler"
    studentLastName = "Rynear"
    studentSectionNumber = "002"
    studentNetId = "kryne001"
    info = 'FirstName: ' + studentFirstName + '\n'
    info = info + 'LastName: ' + studentLastName + '\n'
    info = info + 'Section: ' + studentSectionNumber + '\n'
    info = info + 'NetId: ' + studentNetId + '\n'
    info = info + 'Python version: ' + pythonVersion + '\n'
    return info

def DNASeqAlignment(DNASeq1,DNASeq2,outputPath):
    similarityScore = -1
    sequenceAlignment1 = ''
    sequenceAlignment2 = ''

    #making file objects
    #seq1_obj = open(DNAseq1, 'r')
    #seq2_obj = open(DNAseq2, 'r')
    
    #reading file objects to obtain strings from each file
    #seq1_str = seq1_obj.read()
    #seq2_str = seq2_obj.read() 

    #convert strings into lists
    #seq1 = list(seq1_str)
    #seq2 = list(seq2_str)
    
    #creating empty table to fill
    #len_seq1 = len(seq1)
    #len_seq2 = len(seq2)

    #########################################################################################
    # Compute new values for similarityScore and sequenceAlignment1 and sequenceAlignment2  #                                                                  #
    ##########################################################################################

    #make dnaseq2 x dnaseq1 matrix

    table = [[0.0 for i in range(len(DNASeq1) + 1)] for j in range(len(DNASeq2) + 1)]
    table_dir = [[0.0 for i in range(len(DNASeq1) + 1)] for j in range(len(DNASeq2) + 1)]
    penalty = 0
    #fill in first row
    for i in range(len(DNASeq1) + 1): 
      table[0][i] = penalty
      table_dir[0][i] = 1
      #table[i][0] = penalty
      penalty = round(penalty - 0.2, 2)

    penalty = 0
    #fill in first column    
    for i in range(len(DNASeq2) + 1):
        table[i][0] = penalty
        table_dir[i][0] = 2
        penalty = round(penalty - 0.2, 2) 

    #fill in table
    for i in range(1, len(DNASeq1) + 1):
        for j in range(1, len(DNASeq2) + 1):
     
            first_check = round(table[i-1][j-1] + pen(DNASeq1[i-1], DNASeq2[j-1]), 2)
            second_check = round(table[i][j-1] - 0.2, 2)
            third_check = round(table[i-1][j] - 0.2, 2)
            if first_check > second_check:
                value2 = first_check
                table[i][j] = value2 
                table_dir[i][j] = 3
            else:
                value2 = second_check
                table[i][j] = value2 
                table_dir[i][j] = 1
            if third_check > value2:
                value2 = third_check
                table[i][j] = value2 
                table_dir[i][j] = 2

        
    x = len(DNASeq1)
    y = len(DNASeq2) 
    similarityScore = table[x][y] 

    
    #traceback
    i = len(DNASeq1) - 1
    j = len(DNASeq2) - 1

    
    

    while (i != 0 and j != 0) :
        if table_dir[i][j] == 1: 

            sequenceAlignment1  = DNASeq2[j] + sequenceAlignment1
            sequenceAlignment2 = "-" + sequenceAlignment2
            j = j-1
        elif table_dir[i][j] == 2: 
            sequenceAlignment2  = DNASeq1[i] + sequenceAlignment2
            sequenceAlignment1 = "-" + sequenceAlignment1
            i = i - 1
        elif table_dir[i][j] == 3:
            sequenceAlignment2  = DNASeq2[i] + sequenceAlignment2
            sequenceAlignment1 = DNASeq1[j] + sequenceAlignment1
            i = i - 1
            j = j - 1


    
    #################################  Output Section  ######################################
    print "similarity score = " + str(similarityScore) + '\n'
    result = "Similarity score: " + str(similarityScore) + '\n'
    result = result + "Sequence alignment1: " + sequenceAlignment1 + '\n'
    result = result + "Sequence alignment2: " + sequenceAlignment2 + '\n'
    writeToFile(outputPath,result)
    
def writeToFile(filePath, content):
    with open(filePath,'a') as file:
        file.writelines(content)

def readFile(filePath):
    logLines = ''
    with open(filePath,'r') as file:
        for logText in file:
            logLines = logLines + logText

    uniqueChars = ''.join(set(logLines))
    for ch in uniqueChars:
        if ch not in ('A','a','C','c','G','g','T','t'):
            logLines = logLines.replace(ch,'')
    logLines = logLines.upper()
    return logLines

def removeFile(filePath):
    if os.path.isfile(filePath):
        os.remove(filePath)

def pen(var1, var2):
    temp_val = 0
    if (var1 == var2):
        temp_val = 1 
        return temp_val
    
    elif (var1 == 'A' and var2 == 'T'):
        t = -0.15
        return temp_val
    elif (var1 == 'T' and var2 == 'A'):
        temp_val = -0.15
        return temp_val

    elif (var1 == 'G' and var2 == 'C'):
        temp_val = -0.15
        return temp_val
    elif (var1 == 'C' and var2 == 'G'):
        temp_val = -0.15
        return temp_val

    elif (var1 == 'A' and var2 == 'G'):
        temp_val = -0.1
        return temp_val
    elif (var1 == 'G' and var2 == 'A'):
        temp_val = -0.1
        return temp_val

    elif (var1 == 'A' and var2 == 'C'):
        temp_val = -0.1
        return temp_val
    elif (var1 == 'C' and var2 == 'A'):
        temp_val = -0.1
        return temp_val

    elif (var1 == 'G' and var2 == 'T'):
        temp_val = -0.1
        return temp_val
    elif (var1 == 'T' and var2 == 'G'):
        temp_val = -0.1
        return temp_val

    elif (var1 == 'C' and var2 == 'T'):
        temp_val = -0.1
        return temp_val
    elif (var1 == 'T' and var2 == 'C'):
        temp_val = -0.1
        return temp_val

    else:
        return 0 


class index:
    def __init__(self):
        self.value = value
        self.direction = direction


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNA sequence alignment')
    parser.add_argument('DNASeq1FilePath', type=str, help='Path to the file that contains First DNA sequence')
    parser.add_argument('DNASeq2FilePath', type=str, help='Path to the file that contains Second DNA sequence')
    parser.add_argument('OutputFilePath', type=str, help='Path to the output file')
    args = parser.parse_args()
    DNASeq1 = readFile(args.DNASeq1FilePath)
    DNASeq2 = readFile(args.DNASeq2FilePath)
    outputPath = args.OutputFilePath
    removeFile(outputPath)
    writeToFile(outputPath,studentInfo())
    DNASeqAlignment(DNASeq1,DNASeq2,outputPath)








