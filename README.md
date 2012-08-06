# tviz
Visualize a 3D trajectory using Blender.

# Dependecies
Tested under __Mac OS X Lion__ with __Blender 2.63a__ and __Python 3.2.1__.

# Quickstart
Start Blender, go to _Scripting_ mode, and load the code in the _Text Editor_.  Update the `source` variable with the __full path__ to your data, and hit the _Run Script_ button.

# Data format
Data must be a plain text file containing a valid representation of a __list of tuples__ in Python, each tuple having __three float__ components.

## Example
`[(37.00, 10.17, 0.40), (38.00, 10.26, 0.81), (39.00, 10.35, 1.21)]`

# References
1. http://www.blender.org/documentation/blender_python_api_2_63_17