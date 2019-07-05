import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API_linux",
    version="0.0.1A",
    scripts=['apilinux/apilinux'] ,
    author="Jonathan Arrance",
    author_email="jonathan.arrance@gmail.com",
    description="Api linux will allow a user to run linux commands via a REST API interface.",
    long_description=long_description,
    url="https://github.com/JonathanArrance/API_linux.git",
    packages=setuptools.find_packages(),
    install_requires=[
          'flask==1.0.2',
          'Jinja2==2.10.1',
          'pyOpenSSL==18.0.0',
          'python-pam>=1.8.4'
      ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
