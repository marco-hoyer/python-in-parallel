from joblib import Parallel, delayed
import logging


class Task(object):
    def __init__(self, number):
        print("init was called")
        self.number = number
        self.logger = logging.getLogger("{}".format(number))

    def log_something(self):
        self.logger.error("this is a log message")


WORK = [Task(1), Task(2), Task(3), Task(4), Task(5), Task(6)]

for item in WORK:
    print(item.__repr__())

print()
print("let the fun part begin")
print()


def to_be_executed_in_parallel(task):
    print("I am the {}. my name is: {}".format(task.number, task.__repr__()))
    task.log_something()
    while True:
        pass


def run_simply_parallel():
    print("simply run in parallel")
    Parallel(n_jobs=10)(delayed(to_be_executed_in_parallel)(i) for i in WORK)


run_simply_parallel()
