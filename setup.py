from setuptools import setup, find_packages

with open("requirements.txt", "r") as infile:
    requirements = [i.strip() for i in infile.readlines()]

with open("VERSION", "r") as infile:
    version = infile.read().strip()

with open("README.md", "r") as infile:
    long_description = infile.read()

setup(
    name="wipeit",
    version=version,
    author="Andrew Mickael",
    author_email="andrew.mickael@gmail.com",
    description="A small CLI to purge your Reddit history.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amickael/wipeit",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": ["wipeit=wipeit.__main__:cli"],
    },
    python_requires=">=3.6",
)
