from setuptools import setup, find_packages

setup(
    name="var_procesor",
    version="0.0.1",
    author="Yj Lin",
    author_email="yjlin2001@gmail.com",
    description="Var_processor is a Python library that can automatically handle common variable operations in projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yu-Jie1669/var_procesor",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "torch",
    ],
)
