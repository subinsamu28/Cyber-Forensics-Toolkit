# core/file_recovery.py
import pytsk3
import os

def recover_deleted_files(image_path, output_dir):
    results = []

    try:
        img_info = pytsk3.Img_Info(image_path)
        fs = pytsk3.FS_Info(img_info)

        directory = fs.open_dir("/")
        for entry in directory:
            if not hasattr(entry, "info") or not hasattr(entry.info, "name"):
                continue

            name = entry.info.name.name.decode("utf-8", errors="ignore")
            if name in [".", ".."]:
                continue

            if entry.info.meta and entry.info.meta.flags & pytsk3.TSK_FS_META_FLAG_UNALLOC:
                try:
                    file_path = os.path.join(output_dir, f"recovered_{name}")
                    with open(file_path, "wb") as f_out:
                        file_attr = entry.read_random(0, entry.info.meta.size)
                        f_out.write(file_attr)
                    results.append(f"Recovered deleted file: {file_path}")
                except Exception as e:
                    results.append(f"Failed to recover {name}: {str(e)}")
    except Exception as e:
        results.append(f"Error: {str(e)}")

    return results if results else ["No deleted files recovered."]
