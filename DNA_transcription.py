import codon_table_mRNA from config.py
import base_pair_DNA_to_RNA from config.py

def transcription(my_seq):
  replacement = []
  lis = list(my_seq)
  for i in lis:
    if i in base_pair_DNA_to_RNA: 
      replacement.append(base_pair_DNA_to_RNA[i]) 
  return replacement
