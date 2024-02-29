##add more info on markers to read cnt file of each cell
cellpath=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction
cd ${cellpath}
marker=/data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s4_marker_creation/cnv_winsize10000_step10000_hq_merged_vs_hifi_markers_myresult_wsize50kb_final.txt
MQ=1
for sample in A;do
	while read r;do
		echo -e ${sample}"\t"${r}
		cd ${cellpath}/sample_${sample}_asCellseparator_40krp/${r}
		paste longctg_${r}_win_marker_read_count_MQ${MQ}.bed ${marker} > longctg_${r}_win_marker_read_count_MQ${MQ}_updated.bed
	done < ${cellpath}/sample_${sample}_asCellseparator_40krp/${sample}_this_barcode_list
done
