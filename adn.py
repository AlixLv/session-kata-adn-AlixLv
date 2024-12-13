
conversion_table = {
'ATA':'I',
'ATC':'I',
'ATT':'I',
'ATG':'M',
'ACA':'T',
'ACC':'T',
'ACG':'T',
'ACT':'T',
'AAC':'N',
'AAT':'N',
'AAA':'K',
'AAG':'K',
'AGC':'S',
'AGT':'S',
'AGA':'R',
'AGG':'R',
'CTA':'L',
'CTC':'L',
'CTG':'L',
'CTT':'L',
'CCA':'P',
'CCC':'P',
'CCG':'P',
'CCT':'P',
'CAC':'H',
'CAT':'H',
'CAA':'Q',
'CAG':'Q',
'CGA':'R',
'CGC':'R',
'CGG':'R',
'CGT':'R',
'GTA':'V',
'GTC':'V',
'GTG':'V',
'GTT':'V',
'GCA':'A',
'GCC':'A',
'GCG':'A',
'GCT':'A',
'GAC':'D',
'GAT':'D',
'GAA':'E',
'GAG':'E',
'GGA':'G',
'GGC':'G',
'GGG':'G',
'GGT':'G',
'TCA':'S',
'TCC':'S',
'TCG':'S',
'TCT':'S',
'TTC':'F',
'TTT':'F',
'TTA':'L',
'TTG':'L',
'TAC':'Y',
'TAT':'Y',
'TAA':'_',
'TAG':'_',
'TGC':'C',
'TGT':'C',
'TGA':'_',
'TGG':'W',
}

sample = [['TACCT', 'CCGAG', 'CTGGT', 'TCGCG', 'TATGA'], ['TACCT', 'CCGAG', 'CTGGT', 'TCGCG', 'TATGA'], ['AAGGC', 'ACACA', 'TTCAG', 'ACCTG', 'GCTAA'], ['CACAT', 'CCTCT', 'ACGAA', 'CCTGG', 'CCAGT'], ['TTTTA', 'TAGAC', 'AGTAC', 'CTGAG', 'CGTGG']]

def main():
    list_data = readFile()
    # three_groups_list = breakThreeNucleotides(list_data)
    # print(three_groups_list)
    # displayFile(three_groups_list)
    # converting(three_groups_list, conversion_table)
    
    twenty_five_groups_list = breakTwentyFiveNucleotides(list_data)
    #print(twenty_five_groups_list)
    #displayFile(twenty_five_groups_list)
    five_groups_list = breakFiveNucleotides(twenty_five_groups_list)
    print(five_groups_list)
    #displayComplexFile(five_groups_list)
    calculateRecurrences(five_groups_list)
  

def readFile():
    with open("data.txt", "r") as file:
       content = file.read()  
    return content

def breakThreeNucleotides(text):
    result = [text[i:i+3] for i in range(0, len(text), 3)]
    return result

def breakTwentyFiveNucleotides(text):
    result = [text[i:i+25] for i in range(0, len(text), 25)]
    return result

def displayFile(text):
    for line in text:
        print(line)

def displayComplexFile(text):
    for line in text:
        print()
        for group in line:
            print(group)        
    
def converting(text, dico):
    for line in text:
        for key, value in dico.items():
            if line == key:
                print(value, end="")   

def breakFiveNucleotides(text):
    lst = []
    for line in text:
        #print(f"🥝 {line}")
        result = [line[i:i+5] for i in range(0, len(line), 5)]
        lst.append(result)
        #print(f"🍉 {result}")
    return lst    

def calculateRecurrences(list):
    index_in_list = 0
    index_in_group = 0
    list_of_nucleotides = ["T", "C", "A", "G"]
    
                
    for sublist in list:
        print(f"🌼 current sublist: {sublist}")  
        for i in list_of_nucleotides:
            counter = [0, 0, 0, 0, 0]
            #print(f"🔥 current letter: {i} ") 
            for group in sublist:
                #print(group)       
                for index, value in enumerate(group):
                    #print(index, " : ", value)
                    if i == value:
                        counter[index] +=1
            print(f"🌸 {i}, {counter}")    
        print()        

                       
            
main()

