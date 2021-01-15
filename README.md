# nvselector
Auto Selector for NVIDIA GPUs

## Installation

```bash
python setup.py install
```

## Usage

```python
from nvselector import autoset_nvgpu

# select 1 gpu with minimal memory utilization rate
autoset_nvgpu(metric="mem", k=1)

# your GPU codes
# ...
```