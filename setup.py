import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytiny",
    version="0.0.1",
    author="Alvaro Azael Rodriguez Rodriguez",
    author_email="azael.rguez96@gmail.com",
    description="PyTiny is an in-memory key–value database written in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/azael_rguez/pytiny",
    packages=setuptools.find_packages(exclude=("tests",)),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)