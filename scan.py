import sys
from pathlib import Path

image_files = list()
video_files = list()
docs_files = list()
music_files = list()
folders = list()
archives = list()
others = list()
unknown = set()
extensions = set()


registered_extensions = {
    'JPEG': image_files,
    'PNG':  image_files,
    'JPG':  image_files,
    'SVG':  image_files,
    'AVI':  video_files,
    'MP4':  video_files,
    'MOV':  video_files,
    'MKV':  video_files,
    'DOC':  docs_files,
    'DOCX': docs_files,
    'TXT':  docs_files,
    'PDF':  docs_files,
    'XLSX': docs_files,
    'PPTX': docs_files,
    'MP3':  music_files,
    'OGG':  music_files,
    'WAV':  music_files,
    'AMR':  music_files,
    'ZIP':  archives,
    'GZ':   archives,
    'TAR':  archives}

def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()

def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('Images', 'Video', 'Music', 'Docs', 'Archive', 'Other'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)

def print_results():
    print(f"images: {image_files}")
    print(f"music: {music_files}")
    print(f"docs: {docs_files}")
    print(f"video: {video_files}")
    print(f"archive: {archives}")
    print(f"others: {others}")
    print(f"All extensions: {extensions}")
    print(f"Unknown extensions: {unknown}")
    print(f"Folder: {folders}")


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    folder = Path(path)

    scan(folder)
    print_results()