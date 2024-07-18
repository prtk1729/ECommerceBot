import setuptools

# stitch the ReadME to render when publishing to pypi
with open("README.md", "r", encoding="utf-8") as f: 
    long_description = f.read()


__version__ = "0.0.0" # required to make changes (add features etc)

# MAKE CHANGES HERE
REPO_NAME = "ecom"
AUTHOR_USER_NAME = "prtk1729"
SRC_REPO = "ecom"
AUTHOR_EMAIL = "prateek.pani4243@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="An Ecom chatbot to answer user queries",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  # Recall Issues in github -> This tracks all the bugs (fixed and non-fixed) 
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

