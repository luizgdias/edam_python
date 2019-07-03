from owlready2 import *

onto = get_ontology("file://EDAM_1.21.owl")
onto.load()
a = list(onto.classes())

# x = onto.search(type = onto.SciPhyProgramExecute)
# print(x)

instances_SciPhyAlignment 		= onto.SciPhyAlignment
instances_SciPhyConverter 		= onto.SciPhyConverter
instances_SciPhyModelGenerator 	= onto.SciPhyModelGenerator
instances_SciPhyProgramExecute	= onto.SciPhyProgramExecute
instances_SciPhyTrimming		= onto.SciPhyTrimming
instances_SciPhyClean			= onto.SciPhyClean

	
print("\n**********")
os.system('rm sciphy_variations.txt')
cont = 1
os.system('touch sciphy_variations.txt')

for sciphy_clean_program in instances_SciPhyClean.instances(): 

	for sciphy_alignment_program in instances_SciPhyAlignment.instances(): 

		for sciphy_converter_program in instances_SciPhyConverter.instances(): 

			for sciphy_trimming_program in instances_SciPhyTrimming.instances(): 

				for sciphy_modelgenerator_program in instances_SciPhyModelGenerator.instances():

					for sciphy_programexecute_program in instances_SciPhyProgramExecute.instances():

						if ((sciphy_alignment_program in sciphy_clean_program.is_suported_by) and (sciphy_trimming_program in sciphy_converter_program.is_suported_by) and (sciphy_programexecute_program in sciphy_modelgenerator_program.is_suported_by)):
							variations = open('sciphy_variations.txt','a')
							variation = (str(cont)+") "+str(sciphy_clean_program) + " -> " + str(sciphy_alignment_program) + " -> " + str(sciphy_converter_program) + " -> " + str(sciphy_trimming_program) + " -> " +str(sciphy_modelgenerator_program) +" -> " + str(sciphy_programexecute_program))
							print(variation)
							variations.write(variation)
							variations.write('\n')
							cont=cont+1


# print("\n1)---Listing Clean Instances---")
# for sciphy_clean_program in instances_SciPhyClean.instances(): 
# 	print("Prgrama -> "+ str(sciphy_clean_program) +" is_suported_by -> " + str(sciphy_clean_program.is_suported_by))

# print("\n2)---Listing Alignment Programs Instances---")
# for sciphy_alignment_program in instances_SciPhyAlignment.instances(): 
# 	print("Prgrama -> "+ str(sciphy_alignment_program) +" is_suported_by -> " + str(sciphy_alignment_program.is_suported_by))

# print("\n3)---Listing Converter Instances---")
# for sciphy_converter_program in instances_SciPhyConverter.instances(): 
# 	print("Prgrama -> "+ str(sciphy_converter_program) +" is_suported_by -> " + str(sciphy_converter_program.is_suported_by))

# print("\n4)---Listing Trimming Instances---")
# for sciphy_trimming_program in instances_SciPhyTrimming.instances(): 
# 	print("Prgrama -> "+ str(sciphy_trimming_program) +" is_suported_by -> " + str(sciphy_trimming_program.is_suported_by))

# print("\n5)---Listing ModelGenerator Instances---")
# for sciphy_modelgenerator_program in instances_SciPhyModelGenerator.instances(): 
# 	print("Programa-> "+str(sciphy_modelgenerator_program) +" is_suported_for -> "+ str(sciphy_modelgenerator_program.is_suported_for))

# print("\n6)---Listing ProgramExecute Instances---")
# for sciphy_programexecute_program in instances_SciPhyProgramExecute.instances():
# 	print("Programa -> "+str(sciphy_programexecute_program) +" is_supported_for -> " + str(sciphy_programexecute_program.is_suported_for)) 

# x = onto.SciPhyModelGenerator.is_suported_for
# print(x)




# 1) Remove_pipe (sciphyClean) 	is_supported_for 	mafft
#								is_supported_by 	muscle
#								is_supported_by 	probcons
# 
# 2) sciphyAlignment 
#					clustalw 	is_supported_by 
#					lobster		is_suported_by
#					mafft 		is_supported_by 	readseq
#					muscle		is_supported_by		readseq
#					probcons	is_supported_by		readseq
#					tcoffee		is_supported_by
#
# 3) sciphyConverter
#					readseq 	is_supported_by 	gblocks
#								is_supported_by		total
#								is_supported_by		trimal
#
# 4) sciphyTriming 
#					gblocks 	is_supported_by 	modelgenerator
#					total		is_supported_by 	modelgenerator
#					trimal		is_supported_by 	modelgenerator
#
# 5) sciphyModelGenerator
#					modelgenerator is_supported_by 
#
# 6) sciphyProgramExecute 
#					mrbayes		is_supported_by 	modelgenerator
#					raxml 		is_supported_by	 	modelgenerator
#					phyml 		is_supported_by 	modelgenerator
#					weighbor	is_supported_by 	modelgenerator
#					PaupMl		is_supported_by
#					Garli		is_supported_by
#					PaupMp		is_supported_by
#					PaupNj		is_supported_by
#
#
#



# 1) Remove_pipe (sciphyClean) 	is_supported_for 	mafft
#								is_supported_by 	muscle
#								is_supported_by 	probcons
# 
# 2) sciphyAlignment 
#					clustalw 	is_supported_by 
#					lobster		is_suported_by
#					mafft 		is_supported_by 	readseq
#					muscle		is_supported_by		readseq
#					probcons	is_supported_by		readseq
#					tcoffee		is_supported_by
#
# 3) sciphyConverter
#					readseq 	is_supported_by 	gblocks
#								is_supported_by		total
#								is_supported_by		trimal
#
# 4) sciphyTriming 
#					gblocks 	is_supported_by 	modelgenerator
#					total		is_supported_by 	modelgenerator
#					trimal		is_supported_by 	modelgenerator
#
# 5) sciphyModelGenerator
#					modelgenerator is_supported_by 
#
# 6) sciphyProgramExecute 
#					mrbayes		is_supported_by 	modelgenerator
#					raxml 		is_supported_by	 	modelgenerator
#					phyml 		is_supported_by 	modelgenerator
#					weighbor	is_supported_by 	modelgenerator
#					PaupMl		is_supported_by
#					Garli		is_supported_by
#					PaupMp		is_supported_by
#					PaupNj		is_supported_by
#
#
#
