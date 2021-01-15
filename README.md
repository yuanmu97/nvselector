# nvselector
Auto Selector for NVIDIA GPUs

## Installation

from source:
```bash
python setup.py install
```

from pypi:
```bash
pip install nvselector --index-url https://pypi.org/simple/
```

## Usage

```python
from nvselector import autoset_nvgpu

# select 1 gpu with minimal memory utilization rate
autoset_nvgpu(metric="mem", k=1)

# your GPU codes
# ...
```
