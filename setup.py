import os
import setuptools

root = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(root, "README.md"), "r", encoding="utf-8") as fh:
    long_description = fh.read()

exec(open(os.path.join(root, "wbn_pytorch/_version.py")).read())

setuptools.setup(
    name="wbn_pytorch",
    version=__version__,
    author="Massimiliano Mancini",
    author_email="massimiliano.mancini@uni-tuebingen.de",
    description="A PyTorch implementation of Weighted Batch Normalization layers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mancinimassimiliano/pytorch_wbn",
    packages=["wbn_pytorch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
    python_requires='>=3.6',
    install_requires=["wbn_cuda"],
    dependency_links=['file:' + os.path.join(root, "cuda#egg=wbn_cuda-"+__version__)]
)
