R1=A_fqfrom10xBam_bxCorrected_R1.fq.gz
R2=A_fqfrom10xBam_bxCorrected_R2.fq.gz
barcode_len=16
minimumRP=40000
min_readpair=20000000
mkdir sample_A_asCellseparator_40krp
cd sample_A_asCellseparator_40krp
/data/zhangxiaohui/03.software/GameteBinning_tetraploid/GameteBinning_tetraploid/dev_bin/asCellseparator 16 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction/A_fqfrom10xBam_bxCorrected_R1.fq.gz /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction/A_fqfrom10xBam_bxCorrected_R2.fq.gz 40000 20000000 ./