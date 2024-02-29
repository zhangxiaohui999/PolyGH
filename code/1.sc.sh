bowtie2 -x /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s3_curated_asm/HiFiasm_ref_6366long_ctgs_selected.fasta -1 trimmed_A_seq4414plus4461_R1.fastq.gz,trimmed_B_seq4414plus4461_R1.fastq.gz -2 trimmed_A_seq4414plus4461_R2.fastq.gz,trimmed_B_seq4414plus4461_R2.fastq.gz -p 30 -S sc.single.sam
samtools view -@ 30 -bS sc.single.sam > sc.single.bam
samtools sort -@ 30 -o gamete_ManualCurated.bam sc.single.bam
java -jar /data/software/bin/picard.jar MarkDuplicates -I gamete_ManualCurated.bam -O gamete_ManualCurated_markeduplicates.bam -M gamete_ManualCurated_marked_dup_metrics.txt
samtools index gamete_ManualCurated_markeduplicates.bam