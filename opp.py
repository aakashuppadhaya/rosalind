string = "ACAACCCATCTAAAATCATTACTGAATACTCGTTCGTCAAGTTCGCGTGGTGGCTAGACTCCCCAGTCGAAGAACAGCGCATGCATAGTATTTCGCACACGGTTGGAGTGGGGAGGTTGATAGCCCCTTACATTATCCTTAATGGGAGGCGTGTCTAGTACTGCAACTAAATGTCGTGACAAGGGAGTCGGCTCTTTGGCACCACGGGAATTTGAGAATTCTATTCGTCCGAGAAAAATTCATTAACCGGAAAAGGATAAGGGCGTTGGTGATTCTATAAGAAGAAGGACTAGATAAGGCCCACACCCTCAAGGAGGCACCATCTGAAGACAGAATGTGAACTTTGGCGTTTAACGGCCACCAGGTACTGGGACTTGCACGTATGTCGCATGTTATCATAATTTAAGTGGATGATAGCCCATAGCTACCTACAATAGCATAACGTTCTCGCAAGCATCGGTAGAGTCGTAGTAGGCTTCCGAGCGACGATAAGCGTGGTCAGCTGGACCACAAGGAGGCCAGTTTCCCATACTAATGCACACGCTAAAGCTCGGCGCGCGTTTCCACATCACCAGTTATAGTACGTGTTTAACCGCCAGGATGCCCTTGCGTGTGGTCACCAAAGGGGCCGCGCGATGTGTTCAGTCGGCAGACGACTCATGGAGTGTAACTCTTCGAACACCGTGGAACCAACCAGTACCTCACGATGGTTTTGGATATGATTCGATAGATGGGCGAGACGCTGGGTGTACAACTGTCCTCTCGTAGGTTCAAGCATAAAAAATAGTACCCGCTCACGTC"
result = ''.join(reversed(string))
#print(result)
li=list(result)
gu=[]
for  i in li:
			if(i=="T"):
				i="A"
				gu.append(i)

			elif i=="A":
				i="T"
				gu.append(i)
			elif i=="C":
				i="G"
				gu.append(i)
			else:
				i="C"
				gu.append(i)
				#w=result.replace("T","A")
str1 = ''.join(gu)
print(str1)



