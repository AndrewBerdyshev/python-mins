from setuptools import Extension, setup
setup(
    name="matrixpower",
    version="1.0.0",
    description="Matrix power calculation",
    author="andrew",
    author_email="lol@balabol.com",
    ext_modules=[
        Extension(
            name="matrixpower",
            sources=["solution.c"],
        ),
    ]
)