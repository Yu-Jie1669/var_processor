from setuptools import setup, find_packages

setup(
    name="var_process",
    version="0.0.1",
    author="Yj Lin",
    author_email="yjlin2001@gmail.com",
    description="Auto process vars in your pipeline.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yu-Jie1669/var_process",
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
