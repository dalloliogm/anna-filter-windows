#!/usr/local/bin/perl

# filters MAF values based on gene positions


# open file of genes to filter
open(GENES, "Genes.txt") || die;
while (my $gene = <GENES>){

     chomp $gene;
     my @genes_pos = split (/\t/, $gene);
     my $inici = $genes_pos[2];
     my $fi = $genes_pos[3];

    open(EXP, "Resultats_lower_daf.txt") || die "no puc obrir el fitxer Resultats_lower_daf.txt\n";

    open (OUTFILE, ">OUT_DAF_lower_filtrat.txt") || die;
    while (<EXP>) {
        chomp $_;
        my @fields = split(/\t/, $_);
        my $gene_id = $fields[3];
        my $window_start = $fields[0];
        my $window_end = $fields[1];
        foreach my $line (@genes_pos)
            {
            print OUTFILE "$_\n" if ($gene_id eq $line and $window_start >= $inici and $window_end <= $fi);
            }
        }
}


close OUTFILE;
exit 0;
