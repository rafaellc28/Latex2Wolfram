import setuptools

if __name__ == '__main__':
	setuptools.setup(
		name='Latex to Wolfram',

		packages=setuptools.find_packages(),
		
		entry_points={
			'console_scripts': [
				'latex2wolfram = latex2wolfram.main:main',
			],
		},
		
		setup_requires=['pytest-runner', 'ply'],
		tests_require=['pytest'],
	)