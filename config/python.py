import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

test_requires = [
    'pytest',
    'pytest-cov',
    'pylint',
    'flake8',
    'pymakehelper',
]

install_requires = [
    'svgwrite',
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
    'pylint',
]

python_requires = ">=3.6"

extras_require = {
}
