with open("large_file_1g", "wb") as out:
    out.seek((5*1024 * 1024 * 1024) - 1)
    out.write(b'\0')
