import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "InShorts"
AUTHOR_USER_NAME = "akshats911"
SRC_REPO = "InShorts"
AUTHOR_EMAIL = "i.akshatsharma911@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package to summarize news articles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akshats911/InShorts",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)