import numpy as np
from python_tsp.heuristics import solve_tsp_simulated_annealing

distance_matrix = np.array([
	[0, 361, 395, 249, 433, 459, 268, 497, 678, 712],
	[361, 0, 35.5, 379, 562, 589, 541, 859, 808, 779],
	[395, 35.5, 0, 413, 597, 623, 511, 732, 884, 855],
	[249, 379, 413, 0, 260, 183, 519, 768, 514, 485],
	[433, 562, 597, 260, 0, 60, 682, 921, 254, 288],
	[459, 589, 623, 183, 60, 0, 708, 947, 308, 342],
	[268, 541, 511, 519, 682, 708, 0, 231, 909, 981],
	[497, 859, 732, 768, 921, 947, 231, 0, 1175, 1210],
	[678, 808, 884, 514, 254, 308, 909, 1175, 0, 30],
	[712, 779, 855, 485, 288, 342, 981, 1210, 30, 0]
])

Cities_index, distance = solve_tsp_simulated_annealing(distance_matrix)
print("Permutation:", Cities_index)
print("Distance:", distance)
