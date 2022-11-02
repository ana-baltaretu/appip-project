import bpy, bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

# This is the actual line of code that adds the cube.
# Magic numbers for rotating 90 degrees, DO NOT CHANGE PLEASE GOD!
bpy.ops.mesh.primitive_cube_add(size=2, location=(0,0,0), scale=(1, 30, 20), rotation=(-6.283/4, 0, 0))

bpy.ops.object.editmode_toggle()

obj = bpy.context.active_object

def create_material(mat_name, diffuse_color=(1,1,1,1)):
    mat = bpy.data.materials.get(mat_name)
    if mat is None:
        mat = bpy.data.materials.new(name=mat_name)
    mat.diffuse_color = diffuse_color
    return mat

def set_material_to_face(mat_name, face_number):
    # Bmesh representation
    bm = bmesh.from_edit_mesh(obj.data)
    bm.faces.ensure_lookup_table()
    
    print(obj.data.materials)
    
    mat = bpy.data.materials.get(mat_name)
    obj.data.materials.append(mat)
        
    # Assign the green Material to the second polygon
    bm.faces[face_number].material_index = 2
    return
    

# Generate 2 demo materials
mat_red = create_material("Red", (1,0,0,1))
mat_green = create_material("Green", (0,1,0,1))

# Append both Materials to the created object
obj.data.materials.append(mat_red)
obj.data.materials.append(mat_green)


bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
set_material_to_face("Imported_Material", 2)
bpy.ops.uv.reset()

bpy.ops.object.mode_set(mode='OBJECT')