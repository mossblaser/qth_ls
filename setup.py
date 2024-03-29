from setuptools import setup, find_packages

with open("qth_ls/version.py", "r") as f:
    exec(f.read())

setup(
    name="qth_ls",
    version=__version__,
    packages=find_packages(),

    # Metadata for PyPi
    url="https://github.com/mossblaser/qth_ls",
    author="Jonathan Heathcote",
    description="Library for watching paths in the Qth meta/ls/ tree.",
    license="GPLv2",
    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="mqtt asyncio home-automation messaging",

    # Requirements
    install_requires=["qth>=0.7.0"],
)
