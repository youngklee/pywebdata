from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='pywebdata',
    version='0.1.0',
    description="all the web's data, one api",
    long_description=readme(),
    url='http://github.com/drousis/pywebdata',
    author='Damon Rousis',
    author_email='admin@damonology.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7'
    ],
    packages=find_packages(),
    package_data={
        'pywebdata': ['services/README']
    },
    install_requires=['requests'],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)