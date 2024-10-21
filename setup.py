from setuptools import setup, find_packages

setup(
    name='mrename',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        "click",
        "rich"
    ],
    author='harexew',
    author_email='me@harexew.ovh',
    description='A tool to rename media files',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: GPL-V3',  # Adjust as needed
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Adjust as needed
)
