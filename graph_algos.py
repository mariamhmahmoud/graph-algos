import argparse
from prims import Prim
from arbitrary_insertion import ArbitraryInsertion
import matplotlib.pyplot as plt

#parse command line
parser = argparse.ArgumentParser(description='Specify which graph algorithm to run.')
parser.add_argument('filename')
parser.add_argument('-p', '--prims' , help="Run Prim's algorithm.", action='store_true')
parser.add_argument('-k', '--kruskals', help="Run Kruskal's algorithm.", action='store_true')
parser.add_argument('-a', '--arbitrary', help="Run Arbitary Insertion TSP algorithm.", action='store_true')
parser.add_argument('-t', '--tsp', help="Run optimal tsp algorithm.", action='store_true')
parser.add_argument('-d', '--djikstas', help="Run Djikstra's algorithm.", action='store_true')
args = parser.parse_args()

#stores all coordinates in file
points = []
with open(args.filename, "r") as file:
	for line in file:
		p = line.split()
		x = (int)(p[0])
		y = (int)(p[1])
		coord = (x, y)
		points.append(coord)


if args.prims:
	p = Prim(points)
	p.algo()
	p.print_plot()
elif args.kruskals:
	pass
elif args.arbitrary:
	a = ArbitraryInsertion(points)
	a.algo()
	a.print_plot()
elif args.tsp:
	pass
else:
	pass