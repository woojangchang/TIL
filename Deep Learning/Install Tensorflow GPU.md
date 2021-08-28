# Install Tensorflow-GPU

- 윈도우 환경
- 그래픽카드 : GTX 1660 Super
- 아나콘다 가상환경에 설치
- 설치 소프트웨어 버전
  - python=3.8.8
  - CUDA=11.2
  - cuDNN=8.1.1 (for CUDA 11.2)
  - tensorflow-gpu=2.5.0

## Install

1. 가상 환경 생성
   - `conda create -n tf25`

2. CUDA, cuDNN 다운로드

3. 다운받은 cuDNN zip 파일을 압축 풀어 나온 CUDA 폴더 안의 파일들을 `C:\Program Files\NVIDIA GPU Computing Toolkit\v11.2`폴더 안에 붙여넣기

4. 시스템 환경변수 Path에 다음 네 가지를 추가 (bin, libnvvp는 자동으로 추가되었음)

   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\bin
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\lib
   - C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2\libnvvp

5. tesorflow 설치

   - `conda activate tf25`

   - `pip install tensorflow-gpu==2.5.0`

6. 설치가 되었는지 확인

   - CUDA 확인 : `nvcc --version`

   - Tensorflow 확인

     ```python
     import tensorflow as tf
     print(tf.__version__) # 버전 확인
     print(tf.test.is_built_with_cuda()) # CUDA로 빌드되는지 확인
     print(tf.test.is_built_with_gpu_support()) # CUDA와 같은 GPU로 빌드되는지 확인
     
     print(tf.test.gpu_device_name()) # 사용 가능한 GPU 기기 출력
     
     print(tf.test.is_gpu_available()) # GPU가 사용되는지 확인
     ```

7. 이후 ipykernel 설치

