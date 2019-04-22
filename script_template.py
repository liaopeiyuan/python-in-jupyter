import gzip
import base64
import os
from pathlib import Path
from typing import Dict


# this is base64 encoded source code
file_data: Dict = {file_data}


for path, encoded in file_data.items():
    print(path)
    path = Path(path)
    path.parent.mkdir(exist_ok=True)
    path.write_bytes(gzip.decompress(base64.b64decode(encoded)))


def run(command):
    os.system('export PYTHONPATH=${PYTHONPATH}:/kaggle/working && ' + command)


run('python setup.py develop --install-dir /kaggle/working')
run('python -m src.make_folds')
run('python -m src.main train model_resnet152_2 --fold 2 --n-epochs 25')
run('python -m src.main predict_test model_resnet152_2')
run('python -m src.make_submission model_resnet152_2/test.h5 submission.csv --threshold 0.1')
