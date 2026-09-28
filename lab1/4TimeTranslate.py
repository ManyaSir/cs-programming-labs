time = int(input())
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - hours * 3600 - minutes * 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
