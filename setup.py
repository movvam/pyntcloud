from setuptools import setup, find_packages

version = '0.0.1'

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='pyntcloud',
    version=version,
    description='Python library for working with 3D point clouds.',
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url='https://github.com/daavoo/pyntcloud',
    author='David de la Iglesia Castro',
    author_email='daviddelaiglesiacastro@gmail.com',
    license='The MIT License',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
    ],
    extras_require={
        'LAS':  ["laspy"],
        'PLOT': ["ipython", "matplotlib", "pyvista"],
        'NUMBA': ["numba"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
