from setuptools import find_packages, setup


# get package version
with open('VERSION') as version_file:
    version = version_file.read().strip()

# assemble requirements
with open('requirements_pkg.txt') as f:
    requirements_pkg = f.read().splitlines()

with open('requirements_dev.txt') as f:
    requirements_dev = f.read().splitlines()

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='registerit',
    description='Register package names on PyPI',
    long_description=readme,
    long_description_content_type='text/markdown',
    version=version,
    license='MIT',
    author='Alex Ioannides',
    author_email='alex@bodyworkml.com',
    url='https://github.com/alexioannides/registerit',
    project_urls={
        'Source': 'https://github.com/alexioannides/registerit',
        'Documentation': 'https://github.com/alexioannides/registerit'
    },
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    python_requires=">=3.7.*",
    install_requires=requirements_pkg,
    extras_require={
        'dev': requirements_dev,
    },
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'registerit=registerit.cli:cli'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.7'
    ]
)
