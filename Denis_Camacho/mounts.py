mount = str(input("into the mount"))


def days_in_month(mount):
    mounts = {'January': 31, 'February': 28, 'March': 30}
    day = "None"
    for mount1, days in mounts.items():
        if mount == mount1:
            day = days
            break
    return day


print days_in_month(mount)
