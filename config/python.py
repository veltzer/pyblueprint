dev_requires = [
    "pypitools",
]
config_requires = [
    "pyclassifiers",
]
install_requires = [
    "svgwrite",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
