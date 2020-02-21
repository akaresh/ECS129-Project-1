import base_pair_DNA from config.py
import my_seq from config.py
import codon_table_DNA from config.py

def reverse(my_seq):
  x = list(my_seq)
  x.reverse()
  #comp=""
  #for i in x:
    #comp = comp + i
  return reverse

def replication(reverse):
  #complementary_string = [base_pair_DNA[y] for y in comp.strip()]
  output = []
  for y in reverse:
    if y in base_pair_DNA:
      output.append(base_pair_DNA[y])
  return output



