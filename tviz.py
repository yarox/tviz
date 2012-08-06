'''
tviz.py

Visualize a trajectory from a given set of 3D coordinates.
'''

from mathutils import Vector
import bpy
import ast



def moved(point, offset):
    return point - offset

def scaled(point, factor):
    return point * factor
    
def load_points(filename):    
    with open(filename) as data:
        points = ast.literal_eval(data.read())
        return [Vector(p) for p in points]

def draw_trajectory(points, radius=0.075, type='POLY'): 
    objname = 'MyTrajectory'
    curvename = 'MyCurve'
    
    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')
    curvedata.dimensions = '3D'
    
    objectdata = bpy.data.objects.new(objname, curvedata)
    objectdata.location = (0, 0, 0)
    bpy.context.scene.objects.link(objectdata)
    
    polyline = curvedata.splines.new(type)
    polyline.points.add(len(points) - 1)

    for i, point in enumerate(points):
        polyline.points[i].co = point.to_4d()
    
    polyline.order_u = len(polyline.points) - 1  
    polyline.use_endpoint_u = True
    
    bpy.ops.curve.primitive_bezier_circle_add()
    circle = bpy.context.scene.objects.active
    circle.scale = [radius] * 3
    
    path = bpy.data.objects[objectdata.name]
    path.data.bevel_object = circle
    
    bpy.context.scene.objects.unlink(circle)


if __name__ == '__main__':
    # Load the point list
    source = '/full/path/to/data.txt'
    points = load_points(source)
    
    # Move and scale the original points
    pivot = 0
    offset = moved(points[pivot], Vector([0, 0, 0]))
    points = [scaled(moved(p, offset), 0.05) for p in points]

    # Draw the trajectory
    draw_trajectory(points)