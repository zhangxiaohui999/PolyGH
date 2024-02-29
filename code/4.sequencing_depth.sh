##Get position-wise sequencing depth
samtools depth -Q 1 -a gamete_ManualCurated.bam sm_ManualCurated.bam HiFi_ManualCurated_clean.bam > otava_Hifiasm_ref_pb_illu_depth.txt
awk '{printf ("%s\t%s\t%s\n", $1, $2, $3+$4+$5)}' otava_Hifiasm_ref_pb_illu_depth.txt > otava_Hifiasm_ref_pb_illu_depth_sum.txt