from setuptools import setup, find_packages

setup(
		name='Reciprocal_link_prediction_comparison',
		version='0.1',
		url='https://github.com/brianpallangyo/Reciprocity_link_prediction_comparison',
		author='BRIAN PALLANGYO',
		packages=find_packages(),
		install_requires=['pandas', 'numpy', 'bs4'],
		entry_points={},
		extras_require={'dev':['flake8',]},
		)
		