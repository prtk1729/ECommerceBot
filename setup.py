from setuptools import find_packages, setup

setup(
    name="EComBot",
    version="0.0.0",
    author="Prateek Pani",
    author_email="prateek.pani4243@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask']
)