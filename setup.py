from setuptools import setup, find_packages
setup(
    name="kinterbasdb",
    version="3.3.0",
    description="Python DB API 2.0 extension for Firebird and Interbase",
    author = "Originally by Alexander Kuznetsov ; and expanded by David S. Rushby with contributions from several others (see docs/license.txt for details).",
    author_email = "woodsplitter@rocketmail.com",
    license = "see docs/license.txt",
    packages=find_packages(),
    include_package_data=True,
)
