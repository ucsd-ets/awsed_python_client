from setuptools import find_packages, setup

setup(
    name="awsed-client",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
