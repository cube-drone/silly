from invoke import run, task
import pkg_resources

@task
def test(ctx):
    # /c/Python27/Scripts/nosetests.exe --with-doctest
    ctx.run("nosetests --with-doctest")

@task
def release(ctx):
    version = pkg_resources.require("silly")[0].version
    print("Release: {release}".format(release=version))
    ctx.run("python setup.py bdist_wheel --universal")
    ctx.run("twine upload dist/silly-{release}-py2.py3-none-any.whl".format(release=version))
