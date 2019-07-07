from owlready2 import *
import os

onto = get_ontology("file://EDAM/EDAM_termos.owl")
onto.load()
a = list(onto.classes())
#print(a)

instances_SciPhyAlignment 		= onto.SciPhyAlignment
instances_SciPhyConverter 		= onto.SciPhyConverter
instances_SciPhyModelGenerator 	= onto.SciPhyModelGenerator
instances_SciPhyProgramExecute	= onto.SciPhyProgramExecute
instances_SciPhyTrimming		= onto.SciPhyTrimming
instances_SciPhyClean			= onto.SciPhyClear
#instances_SciPhyDatasets 		= onto.SciPhyDataSets

os.system('rm sciphy_modules/sciphyclear.txt')
os.system('rm sciphy_modules/sciphyalignment.txt')
os.system('rm sciphy_modules/sciphytrimming.txt')
os.system('rm sciphy_modules/sciphyconverter.txt')
os.system('rm sciphy_modules/sciphymodelgenerator.txt')
os.system('rm sciphy_modules/sciphyprogramexecute.txt')
os.system('touch sciphy_modules/sciphyclear.txt')
os.system('touch sciphy_modules/sciphyalignment.txt')
os.system('touch sciphy_modules/sciphytrimming.txt')
os.system('touch sciphy_modules/sciphyconverter.txt')
os.system('touch sciphy_modules/sciphymodelgenerator.txt')
os.system('touch sciphy_modules/sciphyprogramexecute.tx')


for clearprogram in instances_SciPhyClean.instances():
	clear = open('sciphy_modules/sciphyclear.txt','a')
	clear.write(str(clearprogram.has_input)+" -> "+str(clearprogram)+" -> "+str(clearprogram.has_output)+"\n")
	clear.close()

for alignmentprogram in instances_SciPhyAlignment.instances():
	alignment = open('sciphy_modules/sciphyalignment.txt','a')
	alignment.write(str(alignmentprogram.has_input)+" -> "+str(alignmentprogram)+" -> "+str(alignmentprogram.has_output)+"\n")
	alignment.close()

for trimmingprogram in instances_SciPhyTrimming.instances():
	trimming = open('sciphy_modules/sciphytrimming.txt','a')
	trimming.write(str(trimmingprogram.has_input)+" -> "+str(trimmingprogram)+" -> "+str(trimmingprogram.has_output)+"\n")
	trimming.close()

for convertergprogram in instances_SciPhyConverter.instances():
	converter = open('sciphy_modules/sciphyconverter.txt','a')
	converter.write(str(convertergprogram.has_input)+" -> "+str(convertergprogram)+" -> "+str(convertergprogram.has_output)+"\n")
	converter.close()

for modelgeneratorprogram in instances_SciPhyModelGenerator.instances():
	modelgenerator = open('sciphy_modules/sciphymodelgenerator.txt','a')
	modelgenerator.write(str(modelgeneratorprogram.has_input)+" -> "+str(modelgeneratorprogram)+" -> "+str(modelgeneratorprogram.has_output)+"\n")
	modelgenerator.close()

for programexecuteprogram in instances_SciPhyProgramExecute.instances():
	programexecute = open('sciphy_modules/sciphyprogramexecute.txt','a')
	programexecute.write(str(programexecuteprogram.has_input)+" -> "+str(programexecuteprogram)+" -> "+str(programexecuteprogram.has_output)+"\n")
	programexecute.close()		

os.system('rm derivations/sciphyversions.txt')
os.system('touch derivations/sciphyversions.txt')
for clearprogram in instances_SciPhyClean.instances():
	for alignmentprogram in instances_SciPhyAlignment.instances():
		for trimmingprogram in instances_SciPhyTrimming.instances():
			for converterprogram in instances_SciPhyConverter.instances():
				for programexecuteprogram in instances_SciPhyProgramExecute.instances():
					updatesciphyversion = open("derivations/sciphyversions.txt", "a")
					with open("sciphy_modules/sciphyclear.txt", "r") as file:
						for line in file:
							with open("sciphy_modules/sciphyalignment.txt", "r") as file1:
								for line1 in file1:
									with open("sciphy_modules/sciphytrimming.txt", "r") as file2:
										for line2 in file2:
											with open("sciphy_modules/sciphyconverter.txt", "r") as file3:
												for line3 in file3:
													with open("sciphy_modules/sciphyprogramexecute.txt", "r") as file4:
														for line4 in file4:
															if((str(alignmentprogram.has_input) in line) and (str(trimmingprogram.has_input) in line1) and (str(convertergprogram.has_input) in line2) and (str(modelgeneratorprogram.has_input) in line3) and (str(programexecuteprogram.has_input) in line4)):
																sciphyderivarion = str(clearprogram)+ " -> "+str(alignmentprogram)+" -> "+str(trimmingprogram)+" -> "+(str(convertergprogram))+" -> "+(str(modelgeneratorprogram))+" -> "+(str(programexecuteprogram))+"\n"
																updatesciphyversion.write(sciphyderivarion)
													file4.close()
											file3.close()
									file2.close()
							file1.close()	
					file.close()
					updatesciphyversion.close()								
else:
	derivationnumber = sum(1 for linha in open('derivations/sciphyversions.txt'))
	print("Sciphy derivation process ended successfully!")
	print("Number of sciphy derivations: " +str(derivationnumber))





# 1) sciphyClean (Remove_pipe) 	is_supported_by 	mafft
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
#								is_supported_by		trimal
#
# 4) sciphyTriming 
#					gblocks 	is_supported_by 	modelgenerator
#					total		is_supported_by 	modelgenerator
#					trimal		is_supported_by 	modelgenerator
#
# 5) sciphyModelGenerator
#					modelgenerator is_supported_by 	mrbayes
#													raxml
#													phyml
#													weighbor
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
