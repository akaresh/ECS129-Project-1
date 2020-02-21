import replacement from RNA_transcription.py
import codon_table_mRNA from config.py
import stopped from RNA_ORF.py

'''
def split(replacement):
  comp=""
  for i in replacement:
    comp = comp+i
  x = ([comp[i:i+3] for i in range(0, len(comp), 3)])
  return x'''

def translate_mRNA(stopped):
    lis2 =[]
    
    for element in stopped:
        if element in codon_table_tRNA:
            lis2.append(codon_table_tRNA[element])
    return lis2
	
def listToString(lis2): 
  comp=""

  for i in lis2:
    comp = comp+i

  return comp
  
