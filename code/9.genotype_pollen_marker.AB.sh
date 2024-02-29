##genotype each pollen at each contig marker
##Note 1: "-F 3840" == "-F 256 -F 512 -F 1024 -F 2048", excluding all kinds of non-primary alignment!

##Note 2: MQ=5 is too stringent that it was observed some pollen lost coverage at haplotig markers (where there were primary-reads with MQ=1); need to use MQ1: found with IGV.

#cut -f1-3 /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s4_marker_creation/cnv_winsize10000_step10000_hq_merged_vs_hifi_markers_myresult_wsize50kb_final.txt > cnv_winsize10000_step10000_hq_markers_20221123_wsize50kb_final.bed
MQ=1
cellpath=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction
for sample in A B;do
	while read r;do
		cd ${cellpath}/sample_${sample}_asCellseparator_40krp/${r}
		#samtools view -@ 20 -h -F 3840 -q ${MQ} -bS longctg_${r}_markeduplicates.bam
		#samtools sort -@ 20 -o longctg_${r}_markeduplicates_MQ${MQ}_clean.bam longctg_${r}_markeduplicates.bam
		samtools view -h -F 3840 -q ${MQ} -bS longctg_${r}_markeduplicates.bam | samtools sort -o longctg_${r}_markeduplicates_MQ${MQ}_clean.bam -
		samtools index longctg_${r}_markeduplicates_MQ${MQ}_clean.bam
		bedtools coverage -counts -a /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s4_marker_creation/cnv_winsize10000_step10000_hq_markers_20221123_wsize50kb_final.bed -b longctg_${r}_markeduplicates_MQ${MQ}_clean.bam -bed > longctg_${r}_win_marker_read_count_MQ${MQ}.bed
	done < ${cellpath}/sample_${sample}_asCellseparator_40krp/${sample}_this_barcode_list
done
