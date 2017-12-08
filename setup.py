from setuptools import setup

setup(
    name='gym_armed_bandits',
    version='0.0.1',
    install_requires=['gym', 'numpy'],
    packages=['gym_armed_bandits'],
    description='Environvment built in OpenAI Gym for K Armed Bandits Tasks',
    author='Diego Gomez',
    author_email='diegoalejogm@gmail.com',
    url='https://github.com/diegoalejogm/openai-k-armed-bandits',
    download_url='https://github.com/diegoalejogm/openai-k-armed-bandits/archive/0.0.1.tar.gz', 
    keywords=['machine', 'reinforcement', 'learning', 'bandits', 'openai', 'gym'],
    classifiers=[],
)
