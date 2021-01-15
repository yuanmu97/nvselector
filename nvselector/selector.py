import pynvml
import os 


def autoset_nvgpu(metric="memory", k=1):
    """autoset_nvgpu
    automatically set NVIDIA GPU device

    Args:
        metric (str): memory/utilization
            select the GPU with min(metric)
        k (int): num. of selected devices
    """
    pynvml.nvmlInit()
    gpunum = pynvml.nvmlDeviceGetCount()
    assert(k <= gpunum)
    metric_list = []
    for idx in range(gpunum):
        handle = pynvml.nvmlDeviceGetHandleByIndex(idx)

        if metric in ["util", "utilization"]:
            util_rate = pynvml.nvmlDeviceGetUtilizationRates(handle)
            metric_list.append((util_rate, idx))
        else:
            mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            mem_use_rate = 1.0 - mem_info.free / mem_info.total
            metric_list.append((mem_use_rate, idx))
    # sort the devices with ascending metric
    metric_list = sorted(metric_list, key=lambda x:x[0])
    selected_idx = [str(x[1]) for x in metric_list[:k]]
    # set the visible devices
    os.environ["CUDA_VISIBLE_DEVICES"] = ",".join(selected_idx)