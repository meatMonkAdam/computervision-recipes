# This test is based on the test suite implemented for Recommenders project
# https://github.com/Microsoft/Recommenders/tree/master/tests


import os
import papermill as pm
import pytest
from utils_ic.datasets import Urls, unzip_url
from tests.conftest import path_notebooks

# Unless manually modified, python3 should be the name of the current jupyter kernel
# that runs on the activated conda environment
KERNEL_NAME = "cvbp"
OUTPUT_NOTEBOOK = "output.ipynb"


def test_simple_notebook_run(notebooks):
    notebook_path = notebooks["simple"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(PM_VERSION=pm.__version__),
        kernel_name=KERNEL_NAME,
    )


def test_mnist_notebook_run(notebooks):
    notebook_path = notebooks["mnist"]
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(PM_VERSION=pm.__version__),
        kernel_name=KERNEL_NAME,
    )


def test_01_notebook_run(notebooks):
    notebook_path = notebooks["01_training_introduction"]
    data_path = unzip_url(Urls.recycle_path, overwrite=True)
    pm.execute_notebook(
        notebook_path,
        OUTPUT_NOTEBOOK,
        parameters=dict(PM_VERSION=pm.__version__, DATA_PATH=data_path),
        kernel_name=KERNEL_NAME,
    )
