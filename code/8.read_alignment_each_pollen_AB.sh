#!/bin/bash
cellpath=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction
cd /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction
refgenome=/data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s3_curated_asm/HiFiasm_ref_6366long_ctgs_selected.fasta
for sample in A B;do
	cd ${cellpath}/sample_${sample}_asCellseparator_40krp/
	# get individual barcode list
	echo */ | sed 's/ /\n/g' | sed -e 's/\///g' > ${sample}_this_barcode_list
	# mapping within barcode list
	while read bc;do
		cd ${cellpath}/sample_${sample}_asCellseparator_40krp/${bc}
		R1=`ls part*_${bc}_R1.fq.gz`
		R1=${R1//[[:space:]]/,}
		R2=`ls part*_${bc}_R2.fq.gz`
		R2=${R2//[[:space:]]/,}
		bowtie2 -p 20 -x ${refgenome} -1 ${R1} -2 ${R2} -p 25 -S longctg_${bc}.sam 2> longctg_bowtie2.err
		samtools view -@ 30 -bS longctg_${bc}.sam > longctg_nosort_${bc}.bam
		samtools sort -@ 30 -o longctg_${bc}.bam longctg_nosort_${bc}.bam
		samtools index longctg_${bc}.bam
		java -jar /data/software/bin/picard.jar MarkDuplicates -I longctg_${bc}.bam -O longctg_${bc}_markeduplicates.bam -M longctg_${bc}_marked_dup_metrics.txt
		samtools index longctg_${bc}_markeduplicates.bam
	done < ${sample}_this_barcode_list
	cd /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction
done