#from setuptools import setup
# venv.create_environment(venv_dir)
# venv.

import venv
import subprocess
venv.create(
    ".env",
    False,
    True,
    False,
    True,
    None,
    True
)
subprocess.run(
    [
        ".env/bin/python3",
        '-m',
        'pip',
        'install',
        '-r',
        'requirements.txt'
    ]
)

# where requirements.txt is in same dir as this script
#run(["bin/pip", "install", "-r", os.path.abspath("requirements.txt")], cwd=dir)


# with open('requirements.txt') as f: requirements = f.readlines()

# setup(
#     name='S3 Progressive Backup',
#     version='1.0',
#     author='Vladimri Dimitrov',
#     author_email='author@email.com',
#     description='S3 Progressive Backup',
#     long_description='S3 Progressive Backup',
#     scripts=['backup.py'],
#     install_requires=requirements,
#     entry_points=dict(console_scripts=[
#         'myawesomeapp=backup:main'
#     ])
# )
