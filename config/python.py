import config.project

package_name = config.project.project_name

console_scripts = [
]

setup_requires = [
]

test_requires = [
]

install_requires = [
    'svgwrite',
]

dev_requires = [
    'pypitools',
    'pydmt',
    'pyclassifiers',
]

python_requires = ">=3.6"

extras_require={
#    ':python_version == "2.7"': ['futures'],  # for python2.7 backport of concurrent.futures
}
