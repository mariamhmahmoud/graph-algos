import argparse


#parse command line
parser = argparse.ArgumentParser(description='Specify which graph algorithm to run.')
parser.add_argument('filename')
parser.add_argument('-p', '--prims' , help="Run Prim's algorithm.")
parser.add_argument('-k', '--kruskalls', help="Run Kruskall's algorithm.")
parser.add_argument('-a', '--arbitrary', help="Run Arbitary Insertion TSP algorithm.")
parser.add_argument('-t', '--tsp', help="Run optimal tsp algorithm.")
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
	pass
elif args.kruskalls:
	pass
elif args.arbitrary:
	pass
else:
	pass