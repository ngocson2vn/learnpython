from invoke import Collection, Program
from tester import tasks

program = Program(namespace=Collection.from_module(tasks), version='0.1.1')
