# Graphs for dijsktra

# Useful
inf = float('inf')

# Format of one graph is (graph,start,end)
graphs = (
        ({"A": {"B":1},"B": {"A":1} }, "A", "B"),
        ({"A": {"B":30, "C":20},
                   "B": {"A":30, "C":20, "E":60},
                   "C": {"A":20, "B":20, "D":30},
                   "D": {"C":30, "E":30},
                   "E": {"B":60,"D":30} },
                    "A",
                    "E"),
        ({"A": {"B":2, "C":5},
                   "B": {"A":2, "C":4, "F":7},
                   "C": {"A":5, "B":4, "D":6},
                   "D": {"C":6, "E":3, "F":4},
                   "E": {"D":3, "G":4},
                   "F": {"B":7, "D":4, "G":2},
                   "G": {"E":4, "F":2} },
                    "A",
                    "G"),
        ({'A1': {'A1': 0.0, 'A2': 1.0, 'B1': 1.0, 'B2': 1.41},
          'A2': {'A1': 1.0, 'A2': 0.0, 'A3': 1.0, 'B1': 1.41, 'B2': 1.0, 'B3': 1.41},
          'A3': {'A2': 1.0, 'A3': 0.0, 'A4': 1.0, 'B2': 1.41, 'B3': 1.0},
          'A4': {'A3': 1.0, 'A4': 0.0, 'A5': 1.0, 'B3': 1.41, 'B5': 1.41},
          'A5': {'A4': 1.0, 'A5': 0.0, 'A6': 1.0, 'B5': 1.0, 'B6': 1.41},
          'A6': {'A5': 1.0, 'A6': 0.0, 'A7': 1.0, 'B5': 1.41, 'B6': 1.0, 'B7': 1.41},
          'A7': {'A6': 1.0, 'A7': 0.0, 'A8': 1.0, 'B6': 1.41, 'B7': 1.0, 'B8': 1.41},
          'A8': {'A7': 1.0, 'A8': 0.0, 'A9': 1.0, 'B7': 1.41, 'B8': 1.0, 'B9': 1.41},
          'A9': {'A8': 1.0, 'A9': 0.0, 'B8': 1.41, 'B9': 1.0},
          'B1': {'A1': 1.0, 'A2': 1.41, 'B1': 0.0, 'B2': 1.0, 'C1': 1.0},
          'B2': {'A1': 1.41, 'A2': 1.0, 'A3': 1.41, 'B1': 1.0, 'B2': 0.0, 'B3': 1.0, 'C1': 1.41},
          'B3': {'A2': 1.41, 'A3': 1.0, 'A4': 1.41, 'B2': 1.0, 'B3': 0.0},
          'B5': {'A4': 1.41, 'A5': 1.0, 'A6': 1.41, 'B5': 0.0, 'B6': 1.0, 'C5': 1.0, 'C6': 1.41},
          'B6': {'A5': 1.41, 'A6': 1.0, 'A7': 1.41, 'B5': 1.0, 'B6': 0.0, 'B7': 1.0, 'C5': 1.41, 'C6': 1.0, 'C7': 1.41},
          'B7': {'A6': 1.41, 'A7': 1.0, 'A8': 1.41, 'B6': 1.0, 'B7': 0.0, 'B8': 1.0, 'C6': 1.41, 'C7': 1.0, 'C8': 1.41},
          'B8': {'A7': 1.41, 'A8': 1.0, 'A9': 1.41, 'B7': 1.0, 'B8': 0.0, 'B9': 1.0, 'C7': 1.41, 'C8': 1.0, 'C9': 1.41},
          'B9': {'A8': 1.41, 'A9': 1.0, 'B8': 1.0, 'B9': 0.0, 'C8': 1.41, 'C9': 1.0},
          'C1': {'B1': 1.0, 'B2': 1.41, 'C1': 0.0, 'D1': 1.0, 'D2': 1.41},
          'C5': {'B5': 1.0, 'B6': 1.41, 'C5': 0.0, 'C6': 1.0},
          'C6': {'B5': 1.41, 'B6': 1.0, 'B7': 1.41, 'C5': 1.0, 'C6': 0.0, 'C7': 1.0, 'D7': 1.41},
          'C7': {'B6': 1.41, 'B7': 1.0, 'B8': 1.41, 'C6': 1.0, 'C7': 0.0, 'C8': 1.0, 'D7': 1.0, 'D8': 1.41},
          'C8': {'B7': 1.41, 'B8': 1.0, 'B9': 1.41, 'C7': 1.0, 'C8': 0.0, 'C9': 1.0, 'D7': 1.41, 'D8': 1.0, 'D9': 1.41},
          'C9': {'B8': 1.41, 'B9': 1.0, 'C8': 1.0, 'C9': 0.0, 'D8': 1.41, 'D9': 1.0},
          'D1': {'C1': 1.0, 'D1': 0.0, 'D2': 1.0, 'E1': 1.0, 'E2': 1.41},
          'D2': {'C1': 1.41, 'D1': 1.0, 'D2': 0.0, 'D3': 1.0, 'E1': 1.41, 'E2': 1.0, 'E3': 1.41},
          'D3': {'D2': 1.0, 'D3': 0.0, 'E2': 1.41, 'E3': 1.0, 'E4': 1.41},
          'D7': {'C6': 1.41, 'C7': 1.0, 'C8': 1.41, 'D7': 0.0, 'D8': 1.0, 'E6': 1.41, 'E7': 1.0, 'E8': 1.41},
          'D8': {'C7': 1.41, 'C8': 1.0, 'C9': 1.41, 'D7': 1.0, 'D8': 0.0, 'D9': 1.0, 'E7': 1.41, 'E8': 1.0, 'E9': 1.41},
          'D9': {'C8': 1.41, 'C9': 1.0, 'D8': 1.0, 'D9': 0.0, 'E8': 1.41, 'E9': 1.0},
          'E1': {'D1': 1.0, 'D2': 1.41, 'E1': 0.0, 'E2': 1.0},
          'E2': {'D1': 1.41, 'D2': 1.0, 'D3': 1.41, 'E1': 1.0, 'E2': 0.0, 'E3': 1.0},
          'E3': {'D2': 1.41, 'D3': 1.0, 'E2': 1.0, 'E3': 0.0, 'E4': 1.0},
          'E4': {'D3': 1.41, 'E3': 1.0, 'E4': 0.0, 'E5': 1.0},
          'E5': {'E4': 1.0, 'E5': 0.0, 'E6': 1.0},
          'E6': {'D7': 1.41, 'E5': 1.0, 'E6': 0.0, 'E7': 1.0},
          'E7': {'D7': 1.0, 'D8': 1.41, 'E6': 1.0, 'E7': 0.0, 'E8': 1.0},
          'E8': {'D7': 1.41, 'D8': 1.0, 'D9': 1.41, 'E7': 1.0, 'E8': 0.0, 'E9': 1.0},
          'E9': {'D8': 1.41, 'D9': 1.0, 'E8': 1.0, 'E9': 0.0}},
         'A9','D1'),
        )
    
    