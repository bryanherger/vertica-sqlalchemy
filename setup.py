from setuptools import setup

setup(
    name='sqlalchemy-vertica-python',
    version='0.0.0',
    description='Vertica dialect for sqlalchemy using vertica_python',
    long_description=open("README.rst").read(),
    license="MIT",
    url='https://github.com/LocusEnergy/vertica-sqlalchemy',
    packages=[
        'sqla_vertica_python',
    ],
    entry_points="""
    [sqlalchemy.dialects]
    vertica.vertica_python = sqla_vertica_python.base:VerticaDialect
    """,
    install_requires=[
        'vertica_python'
    ],
)

