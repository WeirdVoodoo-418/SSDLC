import psutil

def system_info():
    # This function will print the logical drives, names, volume label, size and file system type
    # NOTE: This functionality is platform-dependent and works on Windows.
    print("Logical Drive Information:")
    for partition in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be caught due to the disk that isn't ready
            continue
        print(f"  Drive: {partition.device}")
        print(f"  File system type: {partition.fstype}")
        try:
            drive = psutil.disk_usage(partition.mountpoint)
            print(f"  Total Size: {round(drive.total / (1024 * 1024 * 1024)):} GB")
            print(f"  Used: {round(drive.used / (1024 * 1024 * 1024))} GB")
            print(f"  Free: {round(drive.free / (1024 * 1024 * 1024))} GB")
        except PermissionError:
            print("  Access Denied.")
        print()

system_info()