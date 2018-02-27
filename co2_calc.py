import sys
import os.path
import numpy as np
from transport import Transport
from plot import plot

households = 5 if len(sys.argv) < 2 else int(sys.argv[1])
output_folder = '/output' if len(sys.argv) < 3 else sys.argv[2]
input_folder = '/input' if len(sys.argv) < 4 else sys.argv[3]

def km_to_world(km):
    return km / 40000

co2_kg = households * 3000
transport = Transport(co2_kg)

# 1. Print traveling kilometers per transport type.
print("For {} households, Nerdalize reduces CO2 emissions by {:,d} kg per year.".format(households, co2_kg))
print("")
print("This is equivalent to (per person):")
tmpl = "{} {:,.0f} Kilometers by {}, or {:.1f} times around the world 🌍"
print(tmpl.format("🚗", transport.car(), "car", km_to_world(transport.car())))
print(tmpl.format("🚆", transport.train(), "train", km_to_world(transport.train())))
print(tmpl.format("✈️ ", transport.airplane(), "airplane", km_to_world(transport.airplane())))

if os.path.isdir(output_folder):
	# 2. Plot trips per type of transport in a bar chart.
	x = ['Car', 'Train', 'Airplane']
	y = [km_to_world(transport.car()), km_to_world(transport.train()), km_to_world(transport.airplane())]
	plot(x, y,
	    'Type of transportation',
	    'Times around the world',
	    'Equivalent in CO2 emissions, for {} households.'.format(households),
	    output_folder + '/trips.png'
	)
	
	# 3. Read input file and plot amount of trips that could be made for amount of households.
	input_file = input_folder + "/flights.csv"
	if os.path.isfile(input_file):
	    x = []
	    y = []
	    flights = np.genfromtxt(input_file, delimiter=';', names=True, dtype=None, encoding='utf-8')
	    for flight in flights:
	        x.append(flight['flight'])
	        y.append(transport.airplane() / float(flight['distance']))
	    plot(x, y,
	        'Flights',
	        'Number of trips',
	        'The amount of trips you can make by ✈️ per year, for {} households.'.format(households),
	        output_folder + '/flights.png')
