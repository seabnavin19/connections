import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='conn',
    version='0.0.3',
    author='Mike Huls',
    author_email='navin@hotmail.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/seabnavin19/connections.git',
    project_urls = {
        "Bug Tracker": "https://github.com/seabnavin19/connections/issues"
    },
    license='MIT',
    packages=['Connection'],
    install_requires=['requests'],
)