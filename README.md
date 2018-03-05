# CO2 Calculator
Nerdalize is building a different cloud. Rather than putting thousands of servers into a datacenter, we're distributing them over homes. There, homeowners make good use of the residual heat: to heat their home in winter and their shower water in summer.

This Docker image calculates the amount of CO2 saved per year by Nerdalize. By taking an amount of households as input, it outputs the following:

1. Total CO2 savings in kilograms and how many traveling kilometers this corresponds to for different ways of transportation.
2. If a file `flights.csv` is present, a bar chart showing how many airplane trips you could make, based on the different trips specified in the file.


## Usage
Executing just the python file:
```
usage: co2_calc.py [-h] [--input INPUT] [--output OUTPUT] [households]

positional arguments:
  households            number of households (default: 5)

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        input folder (default: /input)
  --output OUTPUT, -o OUTPUT
                        output folder (default: /output)
```

Executing as a Docker container:
```
docker run -v "$PWD":/input -v "$PWD":/output nerdalize/co2-calculator [households]
```

Or simply execute the following if you're not interested in output files:
```
docker run nerdalize/co2-calculator [households]
```
