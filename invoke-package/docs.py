from invoke import task

@task
def clean(c):
    c.run("rm -rf docs/_build")

@task(clean)
def build(c):
    c.run("sphinx-build docs docs/_build")

