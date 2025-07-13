# core/timeline_generator.py
import os
import csv
import time

def generate_timeline(folder_path, csv_output):
    if not os.path.isdir(folder_path):
        return "Invalid folder path."

    entries = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                stats = os.stat(full_path)
                created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_ctime))
                modified = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_mtime))
                accessed = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stats.st_atime))
                entries.append([file, created, modified, accessed])
            except Exception as e:
                entries.append([file, "Error", "Error", "Error"])

    if entries:
        with open(csv_output, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Filename", "Created", "Modified", "Accessed"])
            writer.writerows(entries)

        return f"Timeline generated and saved to: {csv_output}"
    else:
        return "No files found in the selected directory."
