# core/file_carver.py
def carve_files(file_path, output_dir):
    signatures = {
        b'\xFF\xD8\xFF': (b'\xFF\xD9', '.jpg'),
        b'\x50\x4B\x03\x04': (b'\x50\x4B\x05\x06', '.zip'),
        b'%PDF': (b'%%EOF', '.pdf')
    }

    results = []
    with open(file_path, 'rb') as f:
        data = f.read()

    for magic, (end_marker, ext) in signatures.items():
        start = 0
        count = 0
        while True:
            start_index = data.find(magic, start)
            if start_index == -1:
                break
            end_index = data.find(end_marker, start_index + len(magic))
            if end_index == -1:
                break

            end_index += len(end_marker)
            carved_data = data[start_index:end_index]
            output_file = f"{output_dir}/carved_{count}{ext}"
            with open(output_file, 'wb') as out:
                out.write(carved_data)

            results.append(f"Carved: {output_file}")
            count += 1
            start = end_index

    return results if results else ["No files carved."]
