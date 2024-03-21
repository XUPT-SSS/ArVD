1. transformers==4.27.1
2. overrides   ==3.1.0
3. python == 3.8
4. jsonnet==0.20.0
5. aim==2.3.0
6. protobuf==3.20.0


# step1: Extract xsbt sequence from csv file
step1:   python xsbt.py  

# step2: Normalization
step2：  python norm_test.py   

# step3  Add data path
step3：   Add training set and validation set paths to transfer_paprms.py
# step4:  train
step4: python -m allennlp train \
-s /home/yons/person/zc/ArVD/model/save/.aim/baseline-warp_0-microsoft/unixcoder-base-nine1  /home/yons/person/zc/ArVD/model/configs/warp.jsonnet


