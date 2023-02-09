import argparse
import datetime
import os
import random
import time

unixtime = int

now = datetime.datetime.now()

argparser = argparse.ArgumentParser(description='The simplest tool for deferred commits')

argparser.add_argument('-m', '--msg', type=str, help='commit message')

argparser.add_argument('--minutes', type=int, default=0, help='after how many minutes to commit, relative')
argparser.add_argument('--absminutes', type=int, default=0, help='after how many minutes to commit, absolute')

argparser.add_argument('--hours', type=int, default=0, help='after how many hours to commit, relative')
argparser.add_argument('--abshours', type=int, default=0, help='after how many hours to commit, absolute')

argparser.add_argument('--days', type=int, default=0, help='after how many days to commit, relative')
argparser.add_argument('--absdays', type=int, default=0, help='after how many days to commit, absolute')

argparser.add_argument('--months', type=int, default=0, help='after how many months to commit, relative')
argparser.add_argument('--absmonths', type=int, default=0, help='after how many months to commit, absolute')

argparser.add_argument('--randtime', action='store_true', help='random commit time')

args = argparser.parse_args()


def generate_commit_time(arguments) -> unixtime:
    minutes: int = 0
    hours: int = 0
    days: int = 0
    months: int = 0

    if arguments.randtime:
        minutes = random.randint(0, 59)
        hours = random.randint(0, 23)
    else:
        if arguments.minutes:
            minutes = (now + datetime.timedelta(minutes=arguments.minutes)).minute
        elif arguments.absminutes:
            minutes = arguments.absminutes
        else:
            minutes = now.minute

        if arguments.hours:
            hours = (now + datetime.timedelta(hours=arguments.hours)).hour
        elif arguments.abshours:
            hours = arguments.abshours
        else:
            hours = now.hour

    if arguments.days:
        days = (now + datetime.timedelta(days=arguments.days)).day
    elif arguments.absdays:
        days = arguments.absdays
    else:
        days = now.day

    if arguments.months:
        months = (now + datetime.timedelta(days=arguments.months * 30)).month
    elif arguments.absmonths:
        months = arguments.absmonths
    else:
        months = now.month

    return int(time.mktime(datetime.datetime(
        year=now.year,
        month=months,
        day=days,
        hour=hours,
        minute=minutes,
        second=now.second
    ).timetuple()))


def create_commit(arguments, commit_time: unixtime):
    os.system(f'git commit -m "{arguments.msg}" --date="{commit_time}"')


if __name__ == '__main__':
    commit_time: unixtime = generate_commit_time(args)
    create_commit(args, commit_time)
