import bpy, bmesh
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector
import subprocess
import sys
import os

# TODO: HERE INPUT WIDTH, HEIGHT, SRC IMAGE NAME, NORMAL IMAGE, SPEC IMAGE

normal_image_name = "4_normal_map.jpg"
specularity_image_name = "5_specularity_map.png"
textured_image_name = "6_applied_texture.jpg" # "nefertitti_waves.png"

# Files directory
images_directory = "//..\\output\\latest_run//"

# Images
normal_img = bpy.data.images.load(images_directory + normal_image_name)
spec_img = bpy.data.images.load(images_directory + specularity_image_name)
src_img = bpy.data.images.load(images_directory + textured_image_name)

W, H = src_img.size[1], src_img.size[0]
# Setting rendering resolution for different shapes
bpy.context.scene.render.resolution_x = H
bpy.context.scene.render.resolution_y = W

# Add a new cube if it doesnt exist
objects = bpy.data.objects
if len(objects) < 2:
    # TODO: Change this to flexible size
    part_w = W/30
    part_h = H/30
    mx_w_h = max(part_w, part_h)
    print(mx_w_h)
    new_w = W/mx_w_h
    new_h = H/mx_w_h
    print(new_w, new_h)
    # This is the actual line of code that adds the cube. Magic numbers for rotating 90 degrees
    # DO NOT CHANGE PLEASE GOD!
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0,0,0), scale=(1, new_w, new_h), rotation=(-6.283/4, 0, 0)) 

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
    
    if len(obj.data.materials) < 1:
        obj.data.materials.append(mat)
        
    # Assign the green Material to the second polygon
    bm.faces[face_number].material_index = 2
    return

bpy.ops.object.mode_set(mode='EDIT')

bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
set_material_to_face("Imported_Material", 0)
bpy.ops.uv.reset()

bpy.ops.object.mode_set(mode='OBJECT')



mat = bpy.data.materials.get("Imported_Material")
for k,v in mat.node_tree.nodes.items():
    if "Image Texture" in k and v.label == "NORMAL_MAP_INPUT":
        print("This is normal map", k, v.label)
        v.image = normal_img
    if "Image Texture" in k and v.label == "SPECULARITY_INPUT":
        print("This is specularity map", k, v.label)
        v.image = spec_img
    if "Image Texture" in k and v.label == "SOURCE_INPUT_IMAGE":
        print("This is input image", k, v.label)
        v.image = src_img
 