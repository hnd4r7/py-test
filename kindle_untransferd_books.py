import os


def get_book_name(text):
    # Chinese character range (basic CJK Unified Ideographs: U+4E00–U+9FFF)
    # English character range (a-z, A-Z)
    res = ""
    for char in text:
        if (0x4E00 <= ord(char) <= 0x9FFF) or char.isalpha():
            res += char
        else:
            break
    return res


def get_kindle_files(d):
    files = []
    for root, _, filenames in os.walk(d):
        for f in filenames:
            if f.endswith(".azw3") or f.endswith(".epub"):
                files.append((f, get_book_name(f)))  # Store full path
    return files


backup = get_kindle_files(r"E:\Kindle-BACKUP\documents\Downloads\Items01")
used = get_kindle_files(r"D:\Documents\---")

# Optional: Print results
res = set()
for f in set((f[1] for f in backup)) - set((f[1] for f in used)):
    for i in backup:
        if f == i[1]:
            res.add(i[0])
for i in res:
    print(rf"E:\Kindle-BACKUP\documents\Downloads\Items01\{i}")
