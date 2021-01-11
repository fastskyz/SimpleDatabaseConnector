import setuptools

'''
install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir.req) for ir in install_reqs]

with open("requirements.txt", "r", encoding="utf-16") as fh:
    requirements = [str(line).rstrip() for line in fh.readlines()]
'''

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simple-sql-connector",
    version="0.0.3",
    author="fastskyz",
    author_email="seppedelanghe17@gmail.com",
    description="A simple SQL Connector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastskyz/SimplePythonSQLConnector ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "pyodbc==4.0.30",
        "uuid==1.30"
    ]
)