bowtie2 -x /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s3_curated_asm/HiFiasm_ref_6366long_ctgs_selected.fasta -1 trimmed_C_seq2806_R1.fastq.gz -2 trimmed_C_seq2806_R2.fastq.gz -p 30 -S sm.link.sam
samtools view -@ 30 -bS sm.link.sam > sm.link.bam
samtools sort -@ 30 -o sm_ManualCurated.bam sm.link.bam
java -jar /data/software/bin/picard.jar MarkDuplicates -I sm_ManualCurated.bam -O sm_ManualCurated_markeduplicates.bam -M sm_ManualCurated_marked_dup_metrics.txt
samtools index sm_ManualCurated_markeduplicates.bam