from utils import open_test_file, close_test_file, get_line
from solve import sort_playlist_by_flow

TEST_FILE = None  # Cambiar a "test1.txt" para pruebas locales


inp = open_test_file(TEST_FILE)

first = get_line(inp)
n = int(first.strip())
tracks = []
cols = None
for _ in range(n):
    line = get_line(inp)
    parts = line.strip().split()
    if cols is None:
        cols = len(parts)
    title = parts[0]
    bpm = int(parts[1])
    if len(parts) == 3:
        energy = int(parts[2])
        tracks.append((title, bpm, energy))
    else:
        tracks.append((title, bpm))

use_energy = (cols == 3)
sorted_titles = sort_playlist_by_flow(tracks, use_energy)

print(f"[{', '.join(sorted_titles)}]")

close_test_file(TEST_FILE, inp)
