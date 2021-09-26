bl_info = {
    "name": "Add Base",
    "author": "James Torres",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Base",
    "warning": "",
    "doc_url": "",
    "category": "Add Mesh",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatVectorProperty
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector


def add_object(self, context):
    scale_x = self.scale.x
    scale_y = self.scale.y
    scale_z = self.scale.z

    list_verts = [Vector((2.0, 2.0, 2.0)), Vector((0.0, 0.0, 0.0)), Vector((0.0, 0.0, 2.0)), Vector((0.0, 2.0, 0.0)), Vector((2.0, 0.0, 0.0))]
    
    verts = []
    for n in range(len(list_verts)):
        verts.append(((list_verts[n][0] * scale_x, list_verts[n][1] * scale_y, list_verts[n][2] * scale_z)))

    edges = [[0,1],(1,2),(1,3),(1,4)]
    
    faces = []
    
    mesh = bpy.data.meshes.new(name="Velocity_base")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_base"
    bl_label = "Add Base Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="Scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.edges[0].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.measureit.addsegment()
        bpy.data.scenes["Scene"].measureit_gl_show_n=True
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].glspace = 0.00
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].glarrow_a = '2'
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].glcolor = (1, 1, 1, 1)
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].glwidth = 2
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].gladvance = False
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].gldist = False
        bpy.context.object.MeasureGenerator[0].measureit_segments[0].gltxt = "V"
        



        
        add_object(self, context)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.edges[1].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.measureit.addsegment()
        bpy.context.object.MeasureGenerator[0].measureit_segments[1].glspace = 0.00
        bpy.context.object.MeasureGenerator[0].measureit_segments[1].glarrow_b = '2'
        bpy.context.object.MeasureGenerator[0].measureit_segments[1].glcolor = (0, 0, 1, 1)
        bpy.context.object.MeasureGenerator[0].measureit_segments[1].gldist = False
        bpy.context.object.MeasureGenerator[0].measureit_segments[1].gltxt = "Vz"
                
        add_object(self, context)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.edges[2].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.measureit.addsegment()
        bpy.context.object.MeasureGenerator[0].measureit_segments[2].glspace = 0.00
        bpy.context.object.MeasureGenerator[0].measureit_segments[2].glarrow_b = '2'
        bpy.context.object.MeasureGenerator[0].measureit_segments[2].glcolor = (0, 1, 0, 1)
        bpy.context.object.MeasureGenerator[0].measureit_segments[2].gldist = False
        bpy.context.object.MeasureGenerator[0].measureit_segments[2].gltxt = "Vy"
        
        add_object(self, context)
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj.data.edges[3].select = True
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.measureit.addsegment()
        bpy.context.object.MeasureGenerator[0].measureit_segments[3].glspace = 0.00
        bpy.context.object.MeasureGenerator[0].measureit_segments[3].glarrow_b = '2'
        bpy.context.object.MeasureGenerator[0].measureit_segments[3].glcolor = (1, 0, 0, 1)
        bpy.context.object.MeasureGenerator[0].measureit_segments[3].gldist = False
        bpy.context.object.MeasureGenerator[0].measureit_segments[3].gltxt = "Vx"                         
        bpy.ops.object.mode_set(mode = 'OBJECT')
        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add Base",
        icon='INDIRECT_ONLY_OFF')


# This allows you to right click on a button and link to documentation
def add_object_manual_map():
    url_manual_prefix = "https://docs.blender.org/manual/en/latest/"
    url_manual_mapping = (
        ("bpy.ops.mesh.add_object", "scene_layout/object/types.html"),
    )
    return url_manual_prefix, url_manual_mapping


def register():
    bpy.utils.register_class(OBJECT_OT_add_object)
    bpy.utils.register_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.append(add_object_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_object)
    bpy.utils.unregister_manual_map(add_object_manual_map)
    bpy.types.VIEW3D_MT_mesh_add.remove(add_object_button)


if __name__ == "__main__":
    register()
