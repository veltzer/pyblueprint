import config.project

package_name = config.project.project_name

test_requires = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "pymakehelper",
]
install_requires = [
    "svgwrite",
]
dev_requires = [
    "pypitools",
    "pydmt",
    "pyclassifiers",
    "pylint",
]

python_requires = ">=3.9"
test_os = ["ubuntu-20.04"]
test_python = ["3.9"]
