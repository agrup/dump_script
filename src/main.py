# create a main with 3 options:
# make a backup of the current 
# restore backup
# list backups
# and help

from src.database import backup_database
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Backup and restore utility')
    parser.add_argument('--backup', action='store_true', help='Make a backup of the current directory')
    parser.add_argument('--restore', action='store_true', help='Restore a backup')
    parser.add_argument('--list', action='store_true', help='List all backups')
    args = parser.parse_args()

    if args.backup:
        if backup_database():
            print("Backup successful")
        else:
            print("Backup failed")
    # elif args.restore:
    #     restore()
    # elif args.list:
    #     list_backups()
    # elif args.help:
    #     print_help()
    else:
        parser.print_help()

