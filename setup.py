from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in txknext/__init__.py
from txknext import __version__ as version

setup(
	name="txknext",
	version=version,
	description="TXK ERPnext Specifics",
	author="ChD Computers",
	author_email="chdcomputers@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
