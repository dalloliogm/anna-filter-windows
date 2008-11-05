
help:
	@echo 'type "make filter" to calculate results/filtered_windows.txt'

filter: results/filtered_windows.txt
	
results/filtered_windows.txt: data/OUT_DAF_lower_filtrat.txt data/Genes.txt src/filter_genes.py
	@cd src; python filter_genes.py --genes data/Genes.txt --windows data/OUT_DAF_lower_filtrat.txt --output results/filtered_windows.txt
	@echo "Results created in $@"
	

