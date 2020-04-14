import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bass",
    version="0.0.0",
    author="Mehdi Rahim",
    author_email="mehdi.rahim@airliquide.com",
    description="Bass model forecast Python Package",
    license="Air Liquide",
    url="http://",
    packages=find_packages(),
    long_description=read('README.md'),
    dependency_links=[],
    requires=["numpy", "scipy", "matplotlib", "pandas"]
)
