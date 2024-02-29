#minimap2 -ax map-pb -t 30 -N 1 --secondary=no HiFiasm_ref_6366long_ctgs_selected.fasta 4396_A_CCS.fastq.gz -o hifi.sam
#samtools view -@ 30 -bS hifi.sam -o hifi.bam
#samtools sort -@ 30 -o HiFi_ManualCurated.bam hifi.bam
#samtools view -h -F 3840 -bS HiFi_ManualCurated.bam | samtools sort -@ 20 -o HiFi_ManualCurated_clean.bam
#samtools depth -Q 1 -a HiFi_ManualCurated_clean.bam > HiFi_ManualCurated_depth_clean.txt
samtools depth -Q 1 -a gamete_ManualCurated.bam sm_ManualCurated.bam HiFi_ManualCurated_clean.bam > otava_Hifiasm_ref_pb_illu_depth.txt
awk '{printf ("%s\t%s\t%s\n", $1, $2, $3+$4+$5)}' otava_Hifiasm_ref_pb_illu_depth.txt > otava_Hifiasm_ref_pb_illu_depth_sum.txt
