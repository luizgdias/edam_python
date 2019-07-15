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

with open('derivations/sciphyversions.txt', 'r') as versions:
	for line in versions:
		print (line) 
versions.close()

trigger = input("Which data flow do you want to edit?\n")
with open('derivations/sciphyversions.txt', 'r') as file:
	for line in file:
		if(trigger in line):
			print("Derivation: "+line)








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
