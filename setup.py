from setuptools import setup, find_packages

with open("requirements.txt", "r") as infile:
    requirements = [i.strip() for i in infile.readlines()]

with open("VERSION", "r") as infile:
    version = infile.read().strip()

setup(
    name="wipeit",
    version=version,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": ["wipeit=wipeit.main:main"],
    },
)
