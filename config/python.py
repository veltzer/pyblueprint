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
test_os = "[ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.6, 3.7, 3.8]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
