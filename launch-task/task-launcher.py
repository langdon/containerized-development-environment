#!/usr/bin/python
import webbrowser
import argparse
import os

parser = argparse.ArgumentParser(description='launch a task')
parser.add_argument('projects_root', metavar='projects-root', nargs='?', default="", help='root directory of status files')
parser.add_argument('task_name', metavar='task-name', nargs='?', default="", help='name of the task to launch')

args = parser.parse_args()
print(dir(args))
path_to_task = os.path.join(args.projects_root, args.task_name, 'status.txt')
print("task: %s" % path_to_task)
with open (path_to_task, 'r') as status_file:
    content = status_file.read()
    urls = content.split()
    for url in urls:
        webbrowser.open(url)
