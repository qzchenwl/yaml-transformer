from setuptools import setup, find_packages

setup(
    name="yaml-transformer",
    version="0.1.0",
    author="qzchenwl",
    author_email="qzchenwl@gmail.com",
    description="A package for enhancing YAML processing with various features.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/qzchenwl/yaml-transformer",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "jq",
        "requests",
        "jsonpath-ng"
    ],
    extras_require={
        'dev': [
            'pytest'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)