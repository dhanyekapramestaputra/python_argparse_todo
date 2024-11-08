import argparse
import os

def create_parser():
    parser = argparse.ArgumentParser(description="Simple To Do App V2")
    subparsers = parser.add_subparsers(dest="command")
    
    #parser to create and add todo text file
    parser_add = subparsers.add_parser("ADD", help="Create account and the first task")
    parser_add.add_argument("account", type=str, help="account")
    parser_add.add_argument("task", help="task to be included")

    #parser to retrieved saved task
    parser_list = subparsers.add_parser("LIST", help="Retrieve tasks")
    parser_list.add_argument("account", help="tasks account name")

    #parser to remove saved task
    parser_remove = subparsers.add_parser("REMOVE", help="remove specified task")
    parser_remove.add_argument("account", help="account name")
    parser_remove.add_argument("index", help="task index to be deleted")

    return parser

def add_task(account, task):
    path = account+".txt"
    with open(path, "a") as file:
        file.write(task + "\n")

def list(account):
    path = account+".txt"
    if os.path.exists(path):
        with open(path, "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    
    else:
        print("No account found.")

def remove(account, index):
    path = account+".txt"
    if os.path.exists(path):
        with open(path, "r") as file:
            tasks = file.readlines()
        with open(path, "w") as file:
            for i, task in enumerate(tasks, start=1):
                print(i, task)
                if i != index:
                    file.write(task)
            print(f"Task {index} deleted.")
        print("task removed succesfully")

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "ADD":
        add_task(args.account, args.task)
        list(args.account)
    elif args.command == "LIST":
        list(args.account)
    elif args.command == "REMOVE":
        remove(args.account, int(args.index))

if __name__ == "__main__":
    main()