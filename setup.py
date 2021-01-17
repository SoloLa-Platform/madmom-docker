import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beat-tracker-wrapper", # Replace with your own username
    version="0.0.1",
    author="ykhorizon",
    author_email="ykhorizon@example.com",
    description="This is a simple wrapper library for beat and down-beat tracking algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SoloLa-Platform/madmom-docker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)