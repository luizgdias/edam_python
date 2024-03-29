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
# instances_SciPhyTrimming		= onto.SciPhyTrimming
instances_SciPhyClean			= onto.SciPhyClear
#instances_SciPhyDatasets 		= onto.SciPhyDataSets

os.system('rm sciphy_modules/sciphyclear.txt')
os.system('rm sciphy_modules/sciphyalignment.txt')
# os.system('rm sciphy_modules/sciphytrimming.txt')
os.system('rm sciphy_modules/sciphyconverter.txt')
os.system('rm sciphy_modules/sciphymodelgenerator.txt')
os.system('rm sciphy_modules/sciphyprogramexecute.txt')
os.system('touch sciphy_modules/sciphyclear.txt')
os.system('touch sciphy_modules/sciphyalignment.txt')
# os.system('touch sciphy_modules/sciphytrimming.txt')
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

# for trimmingprogram in instances_SciPhyTrimming.instances():
# 	trimming = open('sciphy_modules/sciphytrimming.txt','a')
# 	trimming.write(str(trimmingprogram.has_input)+" -> "+str(trimmingprogram)+" -> "+str(trimmingprogram.has_output)+"\n")
# 	trimming.close()

for converterprogram in instances_SciPhyConverter.instances():
	converter = open('sciphy_modules/sciphyconverter.txt','a')
	converter.write(str(converterprogram.has_input)+" -> "+str(converterprogram)+" -> "+str(converterprogram.has_output)+"\n")
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
cont = 1
updatesciphyversion = open("derivations/sciphyversions.txt", "a")
for clearprogram in instances_SciPhyClean.instances():
	for alignmentprogram in instances_SciPhyAlignment.instances():
		for converterprogram in instances_SciPhyConverter.instances():
			for modelgeneratorprogram in instances_SciPhyModelGenerator.instances():
				for programexecuteprogram in instances_SciPhyProgramExecute.instances():
					if((clearprogram.has_output in alignmentprogram.has_input) and (alignmentprogram.has_output in converterprogram.has_input) and (converterprogram.has_output in modelgeneratorprogram.has_input) and (modelgeneratorprogram.has_output in programexecuteprogram.has_input)):
						sciphyderivarion = (str(clearprogram) + " -> " +str(alignmentprogram) +" -> "+ str(converterprogram)+" -> "+str(modelgeneratorprogram)+" -> "+str(programexecuteprogram))
						updatesciphyversion.write(str(cont) + ") "+ sciphyderivarion +"\n")
						cont = cont+1

print("Sciphy derivation process ended successfully!")
print("Number of sciphy derivations: " +str(cont-1))			






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
# 4) sciphyTriming this transformation was removed in this version*
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
