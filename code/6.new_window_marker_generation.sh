##new window marker generation => cnv_winsize10000_step10000_hq_markers_20210712_wsize50kb_final.txt 
#paste用于合并文件的列 paste 指令会把每个文件以列对列的方式，一列列地加以合并
paste cnv_winsize10000_step10000_hq.txt cnv_winsize10000_step10000_hq_HiFi_only.txt | cut -f1-7,12,13 > cnv_winsize10000_step10000_hq_merged_vs_hifi.txt
/data/zhangxiaohui/03.software/GameteBinning_tetraploid/GameteBinning_tetraploid/dev_bin/tig_marker_finder cnv_winsize10000_step10000_hq_merged_vs_hifi.txt 113 30 50000 1123 > tig_marker_finder.log
