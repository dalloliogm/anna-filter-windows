
INPUTFILES = Resultats_daf_lower_95percent Resultats_maf_lower_95percent.txt Resultats_daf_upper_95percent.txt Resultats_daf_upper_95percent
RESULTSDIR = ./results
RESULTFILES = $(addprefix $(RESULTSDIR)/,$(addsuffix .txt,$(INPUTFILES)))

help:
	@echo 'type "make filter" to calculate results/filtered_windows.txt'

filter_all: results/lower_DAF_filtered.txt results/lower_MAF_filtered.txt results/upper_DAF_filtered.txt  results/upper_MAF_filtered.txt


$(RESULTSDIR)/%_filtered.txt: data/%.txt
	python src/filter_genes.py --genes data/Genes.txt --window $^ --output $@

results/lower_DAF_filtered.txt: data/Resultats_lower_daf.txt data/Genes.txt src/filter_genes.py
	python src/filter_genes.py --genes data/Genes.txt --window data/Resultats_lower_daf.txt --output results/lower_DAF_filtered.txt
	@echo "Results created in $@"
	
results/lower_MAF_filtered.txt: data/Resultats_lower_maf.txt data/Genes.txt src/filter_genes.py
	python src/filter_genes.py --genes data/Genes.txt --window data/Resultats_lower_maf.txt --output results/lower_MAF_filtered.txt
	@echo "Results created in $@"
	
results/upper_DAF_filtered.txt: data/Resultats_upper_daf.txt data/Genes.txt src/filter_genes.py
	python src/filter_genes.py --genes data/Genes.txt --window data/Resultats_upper_daf.txt --output results/upper_DAF_filtered.txt
	@echo "Results created in $@"
	
results/upper_MAF_filtered.txt: data/Resultats_upper_maf.txt data/Genes.txt src/filter_genes.py
	python src/filter_genes.py --genes data/Genes.txt --window data/Resultats_upper_maf.txt --output results/upper_MAF_filtered.txt
	@echo "Results created in $@"
	
