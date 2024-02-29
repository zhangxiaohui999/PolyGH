#!/bin/bash
#wd=/data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s11_717_300
#cd ${wd}
#ls /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/sample_*_asCellseparator_40krp/*/longctg_*_win_marker_read_count_MQ1_updated.bed > longctg_list_bed_files.txt
#ls /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/sample_A_asCellseparator_40krp/*/longctg_*_win_marker_read_count_MQ1_updated.bed > longctg_list_bed_files.txt
#ls /data/zhangxiaohui/01.Backups/04_potato/02.assem/00.Gamete_binning/s7_individual_nuclei_extraction/sample_B_asCellseparator_40krp/*/longctg_*_win_marker_read_count_MQ1_updated.bed > longctg_list_bed_files.txt
#>longctg_list_bed_files_selected717.txt
for sample in A B;do
	while read bc;do
		grep ${bc} longctg_list_bed_files.txt >> longctg_list_bed_files_selected240.txt
	done < /data/zhangxiaohui/01.Backups/04_potato/02.assem/01.Gamete_binning/s7_individual_nuclei_extraction/sample_${sample}_asCellseparator_40krp/longctg_s4p3_selected_717_good_nucei_240_lib${sample}.txt
done