mount = str(input("into the mount"))


def days_in_month(mount):
    mounts = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
              'September': 30, 'October': 31, 'November': 30, 'December': 31}
    day = "None"
    for mount1, days in mounts.items():
        if mount == mount1:
            day = days
            break
    return day


print days_in_month(mount)
