import setuptools

setuptools.setup(
    name="ncaa_recruiting", # Replace with your own username
    version="0.0.1",
    author="dlee",
    author_email="dlee@gmail.com",
    description="Package for NCAA FB recruiting analysis",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)