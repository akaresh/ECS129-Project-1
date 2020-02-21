#Finding the longest ORF
#First look for AUG in both mRNA
#can make it more complicated by looking at two separate genes
#base case: only one gene

#splitting every 3: 
'''
import re
output re.output('..', output)
the output should be a string'''
# should split in 3 three first
#find command and do the split by 3
import replacement from DNA_transcription.py


def RNA_ORF (replacement):
  replacement = str(replacement)
  start = replacement.find('AUG')
  replacement = replacement[start:]
  started = ([replacement[i:i+3] for i in range(0, len(replacement), 3)])
  
  position = started.index('UAA') or started.index('UAG') or started.index('UGA')
  stopped = started[:position]
  return stopped

 ''' for i in x:
    if i == 'UAA':
      index1 = x.index(i)
    if i == 'UAG':
      index2 = x.index(i)
    if i == 'UGA'
      index3 = x.index(i)
    else:
        print("No stop codon was found")
        break
    stop_codon = min(index1, index2, index3)'''


    
    
  


'''
  i = 0
  while len(output)!=0:
    if output[0]=='A':
      if output[1]=='U':
        if output[2]=='G':
          
          while (-i) <= len(output):
            if output[-1+i] == 'A' and output[-2+i]== 'G' and output[-3+i] == 'U':
              pass
            elif output[-1+i] == 'A' and output[-2+i]== 'A' and output[-3+i] == 'U':
              pass
            elif output[-1+i] == 'G' and output[-2+i]== 'A' and output[-3+i] == 'U':
              pass
            else:
              i = i-1
              #conceptually wrong, shoud be in-phase
        else:
          output.pop(0)
      else:
        output.pop(0)
    else:
      output.pop(0)

    if output
      if '''


  
