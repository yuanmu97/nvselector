from nvselector import autoset_nvgpu
import os 

autoset_nvgpu(metric="memory", k=2)
print(os.environ["CUDA_VISIBLE_DEVICES"])