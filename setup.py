import setuptools

setuptools.setup(
    # the first three fields are a must according to the documentation
    name='pyblueprint',
    version='0.0.1',
    packages=[
        'pyblueprint',
    ],
    # from here all is optional
    description='draw diagrams using python',
    long_description='draw diagrams using python',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    keywords=[
        'svg',
        'diagram',
        'python',
        'inkscape',
    ],
    url='https://veltzer.github.io/pyblueprint',
    download_url='https://github.com/veltzer/pyblueprint',
    license='MIT',
    platforms=[
        'python3',
    ],
    install_requires=[
        'svgwrite',
    ],
    extras_require={
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
    ],
    data_files=[
    ],
    entry_points={'console_scripts': [
    ]},
    python_requires='>=3.5',
)
