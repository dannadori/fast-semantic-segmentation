# Dockerでtensorflow 1.12以下を作成
```
 docker run --gpus all -v /home/wataru/ssd1/git_work/fast-semantic-segmentation:/work -ti nvidia/cuda:9.0-cudnn7-devel /bin/bash
```

```
$ docker run --gpus '"device=0"' -v /home/wataru/ssd1/git_work/fast-semantic-segmentation:/work -ti nvidia/cuda:9.0-cudnn7-devel /bin/bash
```

```
apt-get update -y ; apt-get install -y mlocate python3 python3-pip;updatedb;pip3 install --upgrade pip
pip3 install tensorflow-gpu==1.12
pip3 install toposort

export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda-9.0/extras/CUPTI/lib64/

```
# 実行
Dockerコンテナの外でコマンドらいい一覧を作っておく。
```
sh setup_my_project.sh
```
コンテナ内で実行。（モデル生成まで）

JS化はコンテナの外。
```
virtualenv venv_tfjs
source venv_tfjs/bin/activate
pip install tensorflowjs



```

# 実行のメモ
train_mem_saving.pyよりtrain.pyのほうが安定している。こちらをつかうこと。