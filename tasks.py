from invoke import run, task

@task
def test():
    # /c/Python27/Scripts/nosetests.exe --with-doctest
    run("nosetests --with-doctest")

@task
def release():
    pass
