from setuptools import setup, find_packages

setup(
    name='synowiz',
    version='1.0.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='SynoWiz unified CLI for Lexico and Practice services',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/fafadoboy/SynoWiz',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',  # Add 'rich' or other packages if needed
    ],
    entry_points={
        'console_scripts': [
            'synowiz=cli.synowiz:synowiz',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
