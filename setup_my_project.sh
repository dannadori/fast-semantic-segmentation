python3 SCRIPT/generate_conf_and_cmds.py  \
	--num_class 2 \
	--num_steps 12000 \
	--height 300 \
	--width 300 \
	--train_num_examples 24340 \
	--eval_num_examples 2870 \
	--filter_scale 0.1 \
	--train_input_path TFRECORDS/train_2434.record \
	--eval_input_path  TFRECORDS/test_287.record   \
	
#	--train_input_path ../FLECT-BARCODE/dataset/DATA004_TFRECORDS_SS/002_icnet2_300x300/train_2434.record \
#	--eval_input_path  ../FLECT-BARCODE/dataset/DATA004_TFRECORDS_SS/002_icnet2_300x300/test_287.record   \


# ※ example数は10度ずつ10回転させているので10倍
#	--train_num_examples 24340 
#	--eval_num_examples 2870


	
