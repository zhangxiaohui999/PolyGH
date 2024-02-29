##index the genome with cellranger-dna
refgenome=potato_dm_v404_all_pm_un.fa
#/data/zhangxiaohui/04.opt/biosoft/cellranger-dna-1.1.0/cellranger-dna mkref potato_dm_v404_all_pm_un.fasta /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/contig_defs.json> 1.json.log

#/data/zhangxiaohui/04.opt/biosoft/cellranger-dna-1.1.0/cellranger-dna cnv --id=A_all3runs --reference=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/refdata-potato_dm_v404_all_pm_un/ --fastq=/data/zhangxiaohui/01.Backups/04_potato/01.data/03.Single_cell/new --sample=4414_A_run633_SI-GA-A1,4461_A_run636_SI-GA-A1 --localcores=40 --localmem=30

#/data/zhangxiaohui/04.opt/biosoft/cellranger-dna-1.1.0/cellranger-dna cnv --id=B_all3runs --reference=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/refdata-potato_dm_v404_all_pm_un/ --fastq=/data/zhangxiaohui/01.Backups/04_potato/01.data/03.Single_cell/new --sample=4414_B_run633_SI-GA-B1,4461_B_run636_SI-GA-B1 --localcores=40 --localmem=30

bam=/data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/A_all3runs/outs/possorted_bam.bam
samtools sort -n ${bam} -o RNsorted_bam.bam
#samtools sort -n -@ 50 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/A_all3runs/outs/possorted_bam.bam -o RNsorted_bam.bam
#samtools sort -n -@ 50 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/B_all3runs/outs/possorted_bam.bam -o RNsorted_bam_B.bam

bam=/data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/RNsorted_bam.bam
#samtools view -@ 50 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/RNsorted_bam.bam | /data/zhangxiaohui/03.software/GameteBinning_tetraploid/GameteBinning_tetraploid/dev_bin/T10xbam2fq - A
#samtools view -@ 50 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_my/RNsorted_bam_B.bam | /data/zhangxiaohui/03.software/GameteBinning_tetraploid/GameteBinning_tetraploid/dev_bin/T10xbam2fq - B

R1=A_fqfrom10xBam_bxCorrected_R1.fq.gz
R2=A_fqfrom10xBam_bxCorrected_R2.fq.gz
barcode_len=16
minimumRP=40000
min_readpair=20000000
mkdir sample_A_asCellseparator_40krp
cd sample_A_asCellseparator_40krp
/data/zhangxiaohui/03.software/GameteBinning_tetraploid/GameteBinning_tetraploid/dev_bin/asCellseparator ${barcode_len} ${R1} ${R2} ${minimumRP} ${min_readpair} ./


##Barcode-specific fastq file(s) will be collected under
#sample_${sample}_asCellseparator_40krp/XXXbarcodeXXX/

##Get list of good barcodes,
awk '$2>=40000' asCellseparator_intermediate_raw_barcode_stat.txt > barcode_over_40000rpairs.list













---------------------------------B----------------------------------------------
/data/zhangxiaohui/04.opt/biosoft/cellranger-dna-1.1.0/cellranger-dna cnv --id=B_all3runs --reference=/data/zhangxiaohui/01.Backups/04_potato/01.data/s7_individual_nuclei_extraction/refdata-potato_dm_v404_all_pm_un/ --fastq=/data/zhangxiaohui/01.Backups/04_potato/01.data/s0_reads/ --sample=4414_B_run633_SI-GA-B1,4461_B_run636_SI-GA-B1 --localcores=40 --localmem=30