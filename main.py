#Enter DNA sequence in 5' to 3' direction
  #check lowercase and uppercase
    #if encounter problem, convert everything uppercase
    #send message "Detected LowerCases, Converted to Uppercase and ran program"
  #check for A,T,G,C only
    #if encounter probelm
    #send message "Detected non-base pair letter, program aborted, please check and retry again", go back out to the beginnger and retry to "Enter DNA Sequence"
    

#my_seq = str(strand)
#my_seq1 = my_seq
#Make a copy of my_seq
#copy of my_seq1 will go thru the dictionary and switches all the letters
#copy of my_seq1 = reverse_rnaseq for complementary variable
#reverse_rnaseq[stringlength::-1] to reverse the whole string
#translate my_seq with dictionary and switches 'T' to 'U' and rename to my_rnaseq
#now we have my_rnaseq and reverse_rnaseq for both reading frame


#use the find function in python to read the 2 strands of mRNA from 5' to 3'
#if find AUG, split the codon in triplets
#after splitting, find stop codon, if no stop codon -> shoot error message
#only the sequence with AUG and stop codon will get translate
#after translate, return a string of amino acid one letter code


#make it user interactive with multiple reminder messages if it runs into errors
#always make reading go from 5'-3'
import transcription from DNA_transcription.py

def checker(my_seq):
    for i in my_seq:
        if i != 'A' and i != 'C' and i != 'T' and i != 'G':
            print("Detected one or more non-DNA base pair letter.\nProgram aborted.\nPlease check your DNA Sequence and retry.\n")
            break

my_seq = input("Please Enter DNA Sequence in 5' to 3' Direction:\n")
x = 0
for i in my_seq:  
    if i.islower() == True:
        my_seq = my_seq.upper()
        x = x+1

if x>=1:
    print('Detected one or more lowercase in DNA Sequence.\nConverted', x ,'lowercase(s) to uppercase(s).\nProgram continue to run.\n')

checker(my_seq)

my_seq1 = my_seq
#my_seq = coding
#my_seq1 = template

transcription(my_seq)
#my_seq as coding strand

reverse(replication(my_seq1))
#this gives coding strand of the template strand and reverse it
#5' to 3'

#check if both replacement and the reverse have ORF?
RNA_ORF(replacement)
if len(RNA_ORF(replacement)) > 1:
  listToString(translate_mRNA(stopped))
else:
  pass
  
RNA_ORF(reverse)
if len(RNA_OFR(reverse)) > 1:
  listToString(translate_mRNA(stopped))
else:
  print('Open Reading Frame was not found')





