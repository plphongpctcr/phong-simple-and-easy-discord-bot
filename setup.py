from setuptools import setup, find_packages

setup(
    name='simple-and-easy-discord-bot',
    version='0.1.1',
    description='simple discord bot by dora-0',
    author='dora-0',
    author_email='55905774+dora-0@users.noreply.github.com',
    url='https://github.com/plphongpctcr/phong-simple-and-easy-discord-bot',
    install_requires=['asyncio', 'websockets', 'aiohttp', 'discord',],
    packages=find_packages(exclude=[]),
    keywords=['dora-0', 'discord', 'python tutorial', 'pypi'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)

