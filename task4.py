tiles = [
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
    ]
def maximum_score(tiles):
    res = 0
    for x in tiles:
        res += x['score']
    return res

print(maximum_score(tiles))
