
# ArVD： Robust Vulnerability Detection with Limited Data via Training-Efficient Adversarial Reprogramming
The substantial increase in software vulnerabilities
poses a significant threat to system security, prompting a surge
of interest in applying deep learning (DL) to vulnerability
detection. However, current DL-based detectors heavily rely
on large-scale labeled data, leading to inefficiency and notable
performance degradation in scenarios with limited data. Fur-
thermore, these detectors often lack robustness against adver-
sarial code transformation attacks. To address these challenges,
this paper proposes ArVD (Adversarial Reprogramming-Based
Vulnerability Detector), which implements a novel and computa-
tionally inexpensive approach to reprogram a pre-trained model
for detecting vulnerabilities at the function level. Specifically,
ArVD first constructs structure-aware token sequences from
source code. Given these inputs, the model then exclusively
learns universal perturbation elements to be added into the token
sequences and leverages self-attention mechanism to enhance
non-linear interactions among tokens and perturbations, such
that the learning capabilities from the pre-trained model can be
adapted to vulnerability detection with less training data and
time yet higher detection effectiveness and robustness. Extensive
experiments conducted on multiple datasets demonstrate that
ArVD significantly reduces the trainable parameters to approxi-
mately 20,000 while outperforming DL-based baselines in terms
of detection effectiveness, data-limited performance, as well as
runtime overhead. Moreover, ArVD effectively counters code
transformation attacks; compared to the state-of-the-art ZigZag
framework that is designed to enhance detector robustness.



# Design of ArVD
<div align=center><img src="https://github.com/SunshineMiles/ArVD/blob/master/frame.png" width="2200" height="250" /></div>

 **ArVD proceeds with the following main steps:**
 -  **_input preparation_:** which converts the given code snippets into structure-aware token sequences as inputs;  
 -  **_input transformation_:**  which introduces perturbation elements into input token sequences and utilizes self-attention mechanism from a pre-trained language model to process these perturbed sequences;  
 - **_label remapping_:**  which maps the output of the original task to the vulnerability detection results;  
 - **_optimization_:**  which updates the perturbation elements and the label remapping layer to adapt the language model for vulnerability detection;


# Datasets
We compare with state-of-the-art methods in the first five experiments, including Baseline-BiLSTM, Baseline-TextCNN, VulCNN, SySeVR, Reveal, and CodeBERT. Four datasets are used, including a Synthetic dataset TrVD. TrVD(https://github.com/XUPT-SSS/TrVD) is a dataset constructed for evaluating the TrVD model, which is composed of C/C++ functions based on the Software Assurance Reference Dataset (SARD), a widely used vulnerability database.Additionally, there are three real-world datasets: D2A, Reveal, and Devign.D2A(https://github.com/ibm/D2A) is a real-world vulnerability dataset created by the IBM Research team. It includes several open-source software projects such as FFmpeg, httpd, Libav, LibTIFF, Nginx, and OpenSSL.Reveal (https://github.com/VulDetProject/ReVeal)is a real-world dataset curated from the Linux Debian kernel and Chromium. It was created to address issues of extensive data duplication and unrealistic distribution of vulnerable categories in existing datasets.Devign(https://dl.acm.org/doi/10.5555/3454287.3455202) is a dataset comprising function-level C/C++ source code from projects QEMU and FFmpeg. It has been manually annotated and verified by security researchers to represent real-world scenarios.In the robustness experiments, we utilized the dataset provided by ZigZag. ZigZag(https://github.com/ZigZagframework/zigzag_framework) is derived from NVD and SARD. Eight adversarial code transformation attacks were applied to 6,803 programs without obfuscating the code through Tigress. This process resulted in 50,562 vulnerable examples and 80,043 non-vulnerable examples.



# The required environment for this project
**Here is the environment required for ArVD. It is recommended to install the versions specified here to avoid potential errors.**

	1. transformers==4.27.1 
	2. overrides==3.1.0 
	3. python==3.8
	4. jsonnet==0.20.0
	5. aim==2.3.0
	6. protobuf==3.20.0
 	7. tree-sitter==0.20.1




# Source Code
# step1: Generates my-languages.so
**Build a custom language library using the tree_sitter library. The library makes it possible to parse source code written in a variety of programming languages using the Tree-sitter parser.**

	python language_build.py

# step2: Normalization
**We use norm_test.py for code normalization, which will generate a new csv file**
	python norm_test.py

# step3: Extract xsbt sequence from csv file
**Application X-SBT traversal Linearize the corresponding tree to a sequence of tags Preserve source structure.**

	python xsbt.py



# step4:  Add data path
	Add training set and validation set paths to transfer_paprms.py
# step5:  Train
**In this step, we will train the model to find the optimal parameters. The model results will be stored in the baseline-warp_0-microsoft/unixcoder-base-nine1 file, and the model's hyperparameters will be set in the warp.jsonnet file. We set the initial learning rate to 0.006 and select the best-performing model, Microsoft/UniXcoder. We use the Adam optimizer with a triangular learning rate schedule, where the warm-up steps constitute 6% of the total training steps. The training will involve 10-20 epochs with a batch size of 16.**

	python -m allennlp train  -s /home/yons/person/zc/ArVD/model/save/.aim/baseline-warp_0-microsoft/unixcoder-base-nine1  /home/yons/person/zc/ArVD/model/configs/warp.jsonnet
