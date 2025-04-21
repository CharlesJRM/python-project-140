from setuptools import setup, find_packages

setup(
    name='hexlet-code',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'brain-games=brain_games.scripts.brain_games:main',
            'brain-even=brain_games.scripts.brain_even:main',
            'brain-calc=brain_games.scripts.brain_calc:main',
            'brain-gcd=brain_games.scripts.brain_gcd:main',
            'brain-prime=brain_games.scripts.brain_prime:main',
            'brain-progression=brain_games.scripts.brain_progression:main',
        ],
    },
    install_requires=[
        'prompt',
    ],
)
