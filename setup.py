from setuptools import setup, find_packages

setup(
    name='network_device_utils',
    version='0.1.0',
    description='Reusable utilities for OUI lookup, device enrichment, and passive device learning in network applications.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'apscheduler',
    ],
    include_package_data=True,
    package_data={
        'network_device_utils': ['data/merged_oui.pkl'],
    },
    python_requires='>=3.7',
    url='https://github.com/yourusername/network_device_utils',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
) 