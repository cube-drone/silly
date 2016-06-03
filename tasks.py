from invoke import run, task
import pkg_resources

@task
def test():
    # /c/Python27/Scripts/nosetests.exe --with-doctest
    run("nosetests --with-doctest")

@task
def release():
    version = pkg_resources.require("silly")[0].version
    print("Release: {release}".format(release=version))
    run("python setup.py bdist_wheel --universal")
    run("twine upload dist/silly-{release}-py2.py3-none-any.whl".format(release=version))
