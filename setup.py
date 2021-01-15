import setuptools

with open("README.md", "r") as fin:
    long_description = fin.read()

setuptools.setup(
    name="nvselector",
    version="0.0.1",
    author="yuanmu",
    author_email="ym0813@mail.ustc.edu.cn",
    description="Auto selector for NVIDIA GPUs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuanmu97/nvselector",
    packages=setuptools.find_packages(),
    install_requires=[
        'pynvml'
    ],
    classifier=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)