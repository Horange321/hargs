import setuptools

setuptools.setup(
    name="hargs",
    version="1.1.1",
    author="Horange",
    author_email="horange321@163.com",
    description="A simple arguments utility",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="github.com/horange321/hargs-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
