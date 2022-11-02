import bpy, bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
import subprocess
import sys
import os

# TODO: HERE INPUT WIDTH AND HEIGHT
W, H = 1877, 1282

# path to python.exe
#python_exe = os.path.join(bpy.app.binary_path)
 
# upgrade pip
#subprocess.call([python_exe, "-m", "ensurepip"])
#subprocess.call([python_exe, "-m", "pip3 install opencv-python"])
 
# install required packages
#subprocess.call([python_exe, "-m", "pip", "install", "opencv-python"])
#import cv2



# IMPORTING CODE FROM ANOTHER FILE!!
#filename = os.path.join(os.path.dirname(bpy.data.filepath), "my_configuration.py")
#exec(compile(open(filename).read(), filename, 'exec'))

bpy.context.scene.render.resolution_x = H
bpy.context.scene.render.resolution_y = W

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

textured_image_name = "nefertitti_waves.png"
bpy.ops.image.open(filepath="//..\\output\\applied_textures\\" + textured_image_name, directory="C:\\Users\\anaba\\OneDrive\\Desktop\\Q1\\_Applied_Image_Processing\\Assignments\\project\\appip-project\\output\\applied_textures\\", files=[{"name":textured_image_name, "name":textured_image_name}], relative_path=True, show_multiview=False)


mat = bpy.data.materials.get("Imported_Material")
for k,v in mat.node_tree.nodes.items():
#    print(k)
    if "Image Texture" in k and v.label == "NORMAL_MAP_INPUT":
        print("This is normal map", k, v.label)
    if "Image Texture" in k and v.label == "SPECULARITY_INPUT":
        print("This is specularity map", k, v.label)
    if "Image Texture" in k and v.label == "SOURCE_INPUT_IMAGE":
        print("This is input image", k, v.label)
        #bpy.data.materials["Imported_Material"].node_tree.nodes[k].label = "aaaaaaaaaaaaaaaaaaa"

        
#    print(v)

#bpy.ops.node.add_file(filepath="C:\\Users\\anaba\\OneDrive\\Desktop\\Q1\\_Applied_Image_Processing\\Assignments\\project\\appip-project\\input\\images\\nefertitti_no_background.png")
#bpy.ops.node.link(detach=False, has_link_picked=False, drag_start=(-137.003, -778.387))

