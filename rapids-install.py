#!/usr/bin/env python
import os, sys, io
import subprocess
from pathlib import Path

print("Starting the RAPIDS install on Colab.  This will take about 15 minutes.")
output = subprocess.Popen(["conda install -y --prefix /usr/local -c rapidsai -c nvidia -c conda-forge cudf=21.06 cuxfilter=21.06 python=3.7 cudatoolkit=11.0 llvmlite gcsfs openssl"], 
    shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

for line in io.TextIOWrapper(output.stdout, encoding="utf-8"):
  if(line == ""):
    break
  else:
    print(line.rstrip())

print("RAPIDS conda installation complete.  Updating Colab's libraries...")
import sys, os, shutil
sys.path.append('/usr/local/lib/python3.7/site-packages/')
os.environ['NUMBAPRO_NVVM'] = '/usr/local/cuda/nvvm/lib64/libnvvm.so'
os.environ['NUMBAPRO_LIBDEVICE'] = '/usr/local/cuda/nvvm/libdevice/'

os.environ["CONDA_PREFIX"] = "/usr/local"
for so in ['cudf', 'rmm', 'nccl', 'cuxfilter', 'cupy']:
  fn = 'lib'+so+'.so'
  source_fn = '/usr/local/lib/'+fn
  dest_fn = '/usr/lib/'+fn
  if os.path.exists(source_fn):
    print(f'Copying {source_fn} to {dest_fn}')
    shutil.copyfile(source_fn, dest_fn)
