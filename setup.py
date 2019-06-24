from setuptools import setup

setup( 
    name='deep_sort',
    
    version='0.10',
    description='Simple Online and Realtime Tracking with a Deep Association Metric',
    url='http://demo.vedalabs.in/',

    # Author details    
    author='Atinderpal Singh',
    author_email='atinderpalap@gmail.com',
    
    license='Commercial',

    packages=['deep_sort', 'deep_sort.deep_sort', 'deep_sort.application_util'],

    install_requires=['numpy'],
    zip_safe=False
    )
