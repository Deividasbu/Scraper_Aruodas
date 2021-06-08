import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='aruodas_scraper',
    version='0.0.1',
    author='Deividas Butkus',
    author_email='deividas.butkus@gmail.com',
    description='www.aruodas.lt scraper for collecting information about the rent of real estate listings',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)