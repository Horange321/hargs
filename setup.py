import setuptools

setuptools.setup(
    name="hargutil",
    version="1.1.3",
    author="Horange",
    author_email="horange321@163.com",
    description="A simple arguments utility",
    long_description=open("README.md", encoding='utf8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/horange321/hargutil-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
