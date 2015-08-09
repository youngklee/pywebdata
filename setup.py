from setuptool import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='pywebdata',
    version='0.1',
    description="all the web's data, one api",
    long_description=readme(),
    url='http://github.com/drousis/pywebdata',
    author='Damon Rousis',
    author_email='admin@damonology.com',
    license='MIT',
    packages=['pywebdata'],
    install_requires=['requests'],
    install_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)