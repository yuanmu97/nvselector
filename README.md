# nvselector
Auto Selector for NVIDIA GPUs

## Installation

```bash
python setup.py install
```

## Usage

```python
from nvselector import autoset_gpu

# select 1 gpu with minimal memory utilization rate
autoset_gpu(metric="mem", k=1)

# your GPU codes
# ...
```