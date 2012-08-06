'''
trajectory.py

Draw a trajectory from a given set of 3D coordinates.
'''

# TODO: Hay que trasladar los puntos hacia el origen.
#   1. Definir un punto origen.
#   2. Tomar un punto de la trayectoria como referencia y hacerlo coincidir 
#      con el origen.         
#   3. Desplazar el resto de puntos acorde con la referencia. 

# TODO: Hay que escalar los puntos segun una constante.
# TODO: Dibujar un plano base.
# TODO: implementarlo como plugin.

#import bpy
import ast



def get_offset(point, origin):
    pass

def move(point, offset):
    pass

def scale(point, factor):
    pass
    
def load_points(filename, factor=1):    
    with open(filename) as data:
        return ast.literal_eval(data.read())
        
#def draw_trajectory(points, radius=1, type='POLY'): 
#    objname = 'MyTrajectory'
#    curvename = 'MyCurve'
#    
#    curvedata = bpy.data.curves.new(name=curvename, type='CURVE')
#    curvedata.dimensions = '3D'
#    
#    objectdata = bpy.data.objects.new(objname, curvedata)
#    objectdata.location = (0, 0, 0)
#    bpy.context.scene.objects.link(objectdata)
#    
#    polyline = curvedata.splines.new(type)
#    polyline.points.add(len(points) - 1)
#
#    for i, point in enumerate(points):
#        polyline.points[i].co = point + (1, )
#    
#    polyline.order_u = len(polyline.points) - 1  
#    polyline.use_endpoint_u = True
#    
#    bpy.ops.curve.primitive_bezier_circle_add()
#    circle = bpy.context.scene.objects.active
#    circle.scale = [radius] * 3
#    
#    path = bpy.data.objects[objectdata.name]
#    path.data.bevel_object = circle
#    
#    bpy.context.scene.objects.unlink(circle)


if __name__ == '__main__'
# Load the point list
points = load_points('/Users/adri/Documents/Sandbox/blender/data.txt')

# Draw the trajectory
draw_trajectory(points)