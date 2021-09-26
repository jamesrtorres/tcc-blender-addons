bl_info = {
    "name": "Add Y Axis",
    "author": "James Torres",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Adds a new Mesh Y Axis",
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

    list_verts = [Vector((-0.05388222634792328, 0.7040677070617676, -0.15957751870155334)), Vector((-0.1014091894030571, 0.7515946626663208, -0.016364900395274162)), Vector((-0.04693589359521866, 0.6971213817596436, 0.13992252945899963)), Vector((-0.050994373857975006, 0.7011798620223999, 0.13992252945899963)), Vector((-0.10295721888542175, 0.7531427145004272, -0.013731149956583977)), Vector((-0.15277282893657684, 0.8029583096504211, 0.13992252945899963)), Vector((-0.1568150371313095, 0.8070005178451538, 0.13992252945899963)), Vector((-0.05763158202171326, 0.7078170776367188, -0.15957751870155334)), Vector((-0.0963086262345314, 0.6616412997245789, -0.15957751870155334)), Vector((-0.14383558928966522, 0.7091682553291321, -0.016364898532629013)), Vector((-0.08936230093240738, 0.6546949744224548, 0.13992252945899963)), Vector((-0.09342078119516373, 0.6587534546852112, 0.13992252945899963)), Vector((-0.14538362622261047, 0.7107163071632385, -0.013731146231293678)), Vector((-0.19519922137260437, 0.7605319023132324, 0.13992252945899963)), Vector((-0.19924142956733704, 0.7645741105079651, 0.13992252945899963)), Vector((-0.10005798935890198, 0.66539067029953, -0.15957751870155334)), Vector((-0.0963086262345314, 0.6616412997245789, -0.15957751870155334)), Vector((-0.08873791247606277, 0.6554548740386963, -0.16575783491134644)), Vector((-0.08052393794059753, 0.6512584090232849, -0.1713332235813141)), Vector((-0.0724707543849945, 0.6494625806808472, -0.17575785517692566)), Vector((-0.06536664068698883, 0.6502432227134705, -0.17859864234924316)), Vector((-0.059907034039497375, 0.6535239219665527, -0.17957749962806702)), Vector((-0.04576489329338074, 0.6676660776138306, -0.17957749962806702)), Vector((-0.042484186589717865, 0.673125684261322, -0.17859864234924316)), Vector((-0.04170353710651398, 0.6802297830581665, -0.17575785517692566)), Vector((-0.04349934309720993, 0.6882830262184143, -0.1713332235813141)), Vector((-0.047695837914943695, 0.6964969635009766, -0.16575783491134644)), Vector((-0.05388222634792328, 0.7040677070617676, -0.15957751870155334)), Vector((-0.14383558928966522, 0.7091682553291321, -0.016364898532629013)), Vector((-0.13829410076141357, 0.7050111293792725, -0.01643059216439724)), Vector((-0.13191071152687073, 0.7026451826095581, -0.01648985594511032)), Vector((-0.1253102868795395, 0.7023021578788757, -0.016536887735128403)), Vector((-0.1191389262676239, 0.7040155529975891, -0.016567084938287735)), Vector((-0.11400070786476135, 0.7076176404953003, -0.01657748967409134)), Vector((-0.09985856711864471, 0.7217597961425781, -0.01657748967409134)), Vector((-0.09625646471977234, 0.7268980145454407, -0.016567084938287735)), Vector((-0.09454308450222015, 0.7330693602561951, -0.016536889597773552)), Vector((-0.09488612413406372, 0.7396697998046875, -0.01648985780775547)), Vector((-0.0972520262002945, 0.746053159236908, -0.01643059402704239)), Vector((-0.1014091894030571, 0.7515946626663208, -0.016364900395274162)), Vector((-0.08936230093240738, 0.6546949744224548, 0.13992252945899963)), Vector((-0.08164377510547638, 0.6483607888221741, 0.1461028754711151)), Vector((-0.07329646497964859, 0.6440309882164001, 0.15167823433876038)), Vector((-0.06513746082782745, 0.6421293616294861, 0.15610286593437195)), Vector((-0.05796542763710022, 0.6428420543670654, 0.15894365310668945)), Vector((-0.05248240381479263, 0.646099328994751, 0.1599225401878357)), Vector((-0.038340263068675995, 0.6602414846420288, 0.1599225401878357)), Vector((-0.03508296608924866, 0.665724515914917, 0.15894365310668945)), Vector((-0.03437025099992752, 0.6728965640068054, 0.15610286593437195)), Vector((-0.03627187758684158, 0.6810555458068848, 0.15167823433876038)), Vector((-0.0406017005443573, 0.6894028782844543, 0.1461028754711151)), Vector((-0.04693589359521866, 0.6971213817596436, 0.13992252945899963)), Vector((-0.09342078119516373, 0.6587534546852112, 0.13992252945899963)), Vector((-0.09548278152942657, 0.6621997952461243, 0.1461028754711151)), Vector((-0.09595862030982971, 0.6666930913925171, 0.15167823433876038)), Vector((-0.09480169415473938, 0.6717935800552368, 0.15610286593437195)), Vector((-0.09212526679039001, 0.6770018935203552, 0.15894368290901184)), Vector((-0.08819132298231125, 0.6818082928657532, 0.1599225401878357)), Vector((-0.07404918968677521, 0.6959503889083862, 0.1599225401878357)), Vector((-0.06924281269311905, 0.6998843550682068, 0.15894368290901184)), Vector((-0.06403448432683945, 0.7025607824325562, 0.15610286593437195)), Vector((-0.05893402546644211, 0.7037177085876465, 0.15167823433876038)), Vector((-0.054440706968307495, 0.7032418847084045, 0.1461028754711151)), Vector((-0.050994373857975006, 0.7011798620223999, 0.13992252945899963)), Vector((-0.14538362622261047, 0.7107163071632385, -0.013731146231293678)), Vector((-0.14460796117782593, 0.71132493019104, 0.0008401507511734962)), Vector((-0.1425238847732544, 0.7132583856582642, 0.013985108584165573)), Vector((-0.13933542370796204, 0.7163273096084595, 0.024417005479335785)), Vector((-0.1353546679019928, 0.720231294631958, 0.031114693731069565)), Vector((-0.1309712827205658, 0.7245882153511047, 0.0334225594997406)), Vector((-0.11682914942502975, 0.7387303709983826, 0.0334225594997406)), Vector((-0.11247221380472183, 0.7431137561798096, 0.031114693731069565)), Vector((-0.1085682138800621, 0.7470945119857788, 0.024417005479335785)), Vector((-0.10549929738044739, 0.7502829432487488, 0.013985104858875275)), Vector((-0.10356588661670685, 0.7523670196533203, 0.000840148888528347)), Vector((-0.10295721888542175, 0.7531427145004272, -0.013731149956583977)), Vector((-0.19519922137260437, 0.7605319023132324, 0.13992252945899963)), Vector((-0.19170315563678741, 0.7584201693534851, 0.1461028754711151)), Vector((-0.18716497719287872, 0.7578994631767273, 0.15167823433876038)), Vector((-0.18202891945838928, 0.7590208053588867, 0.15610286593437195)), Vector((-0.17679771780967712, 0.7616743445396423, 0.15894365310668945)), Vector((-0.17198346555233002, 0.7656004428863525, 0.1599225401878357)), Vector((-0.15784133970737457, 0.7797425389289856, 0.1599225401878357)), Vector((-0.15391527116298676, 0.7845568060874939, 0.15894365310668945)), Vector((-0.15126170217990875, 0.789788007736206, 0.15610286593437195)), Vector((-0.15014038980007172, 0.7949240803718567, 0.15167823433876038)), Vector((-0.15066108107566833, 0.7994622588157654, 0.1461028754711151)), Vector((-0.15277282893657684, 0.8029583096504211, 0.13992252945899963)), Vector((-0.19924142956733704, 0.7645741105079651, 0.13992252945899963)), Vector((-0.20542165637016296, 0.7721386551856995, 0.1461028754711151)), Vector((-0.20961259305477142, 0.7803471088409424, 0.15167823433876038)), Vector((-0.2114039957523346, 0.788395881652832, 0.15610286593437195)), Vector((-0.21062052249908447, 0.7954971194267273, 0.15894365310668945)), Vector((-0.2073388397693634, 0.8009557723999023, 0.1599225401878357)), Vector((-0.19319668412208557, 0.8150979280471802, 0.1599225401878357)), Vector((-0.1877380609512329, 0.8183795809745789, 0.15894365310668945)), Vector((-0.18063679337501526, 0.8191630840301514, 0.15610286593437195)), Vector((-0.17258800566196442, 0.817371666431427, 0.15167823433876038)), Vector((-0.16437959671020508, 0.8131807446479797, 0.1461028754711151)), Vector((-0.1568150371313095, 0.8070005178451538, 0.13992252945899963)), Vector((-0.10005798935890198, 0.66539067029953, -0.15957751870155334)), Vector((-0.10214480757713318, 0.6688618063926697, -0.16575786471366882)), Vector((-0.10264302790164948, 0.673377513885498, -0.1713332235813141)), Vector((-0.1015038788318634, 0.6784957051277161, -0.17575785517692566)), Vector((-0.09883885830640793, 0.6837154626846313, -0.17859864234924316)), Vector((-0.09490884840488434, 0.6885257959365845, -0.17957749962806702)), Vector((-0.0807667076587677, 0.7026678919792175, -0.17957749962806702)), Vector((-0.07595640420913696, 0.7065979242324829, -0.17859864234924316)), Vector((-0.07073666155338287, 0.7092629671096802, -0.17575785517692566)), Vector((-0.06561844050884247, 0.7104020714759827, -0.1713332235813141)), Vector((-0.0611027367413044, 0.70990389585495, -0.16575786471366882)), Vector((-0.05763158202171326, 0.7078170776367188, -0.15957751870155334)), Vector((-1.4901161193847656e-08, 0.6507680416107178, 3.3527612686157227e-08)), Vector((-0.03653799742460251, 0.5046150088310242, -0.03653797507286072)), Vector((0.036537960171699524, 0.5046150088310242, -0.03653797507286072)), Vector((0.07307697832584381, 0.5046150088310242, -0.07307697832584381)), Vector((-0.0730770081281662, 0.5046150088310242, -0.07307697087526321)), Vector((0.036537960171699524, 0.5046150088310242, 0.036538027226924896)), Vector((-0.03653799742460251, 0.5046150088310242, 0.036538027226924896)), Vector((-0.0730770081281662, 0.5046150088310242, 0.07307703047990799)), Vector((0.07307697832584381, 0.5046150088310242, 0.07307702302932739)), Vector((1.4901161193847656e-08, 0.00038498640060424805, 4.6566128730773926e-09))]
    
    verts = []
    for n in range(len(list_verts)):
        verts.append(((list_verts[n][0] * scale_x, list_verts[n][1] * scale_y, list_verts[n][2] * scale_z)))

    edges = []
    
    faces = [[1, 3, 2], [1, 4, 3], [4, 6, 5], [4, 7, 6], [1, 7, 4], [0, 7, 1], [9, 10, 11], [9, 11, 12], [12, 13, 14], [12, 14, 15], [9, 12, 15], [8, 9, 15], [17, 29, 28, 16], [18, 30, 29, 17], [19, 31, 30, 18], [20, 32, 31, 19], [21, 33, 32, 20], [22, 34, 33, 21], [23, 35, 34, 22], [24, 36, 35, 23], [25, 37, 36, 24], [26, 38, 37, 25], [27, 39, 38, 26], [29, 41, 40, 28], [30, 42, 41, 29], [31, 43, 42, 30], [32, 44, 43, 31], [33, 45, 44, 32], [34, 46, 45, 33], [35, 47, 46, 34], [36, 48, 47, 35], [37, 49, 48, 36], [38, 50, 49, 37], [39, 51, 50, 38], [41, 53, 52, 40], [42, 54, 53, 41], [43, 55, 54, 42], [44, 56, 55, 43], [45, 57, 56, 44], [46, 58, 57, 45], [47, 59, 58, 46], [48, 60, 59, 47], [49, 61, 60, 48], [50, 62, 61, 49], [51, 63, 62, 50], [53, 65, 64, 52], [54, 66, 65, 53], [55, 67, 66, 54], [56, 68, 67, 55], [57, 69, 68, 56], [58, 70, 69, 57], [59, 71, 70, 58], [60, 72, 71, 59], [61, 73, 72, 60], [62, 74, 73, 61], [63, 75, 74, 62], [65, 77, 76, 64], [66, 78, 77, 65], [67, 79, 78, 66], [68, 80, 79, 67], [69, 81, 80, 68], [70, 82, 81, 69], [71, 83, 82, 70], [72, 84, 83, 71], [73, 85, 84, 72], [74, 86, 85, 73], [75, 87, 86, 74], [77, 89, 88, 76], [78, 90, 89, 77], [79, 91, 90, 78], [80, 92, 91, 79], [81, 93, 92, 80], [82, 94, 93, 81], [83, 95, 94, 82], [84, 96, 95, 83], [85, 97, 96, 84], [86, 98, 97, 85], [87, 99, 98, 86], [89, 101, 100, 88], [90, 102, 101, 89], [91, 103, 102, 90], [92, 104, 103, 91], [93, 105, 104, 92], [94, 106, 105, 93], [95, 107, 106, 94], [96, 108, 107, 95], [97, 109, 108, 96], [98, 110, 109, 97], [99, 111, 110, 98], [101, 17, 16, 100], [102, 18, 17, 101], [103, 19, 18, 102], [104, 20, 19, 103], [105, 21, 20, 104], [106, 22, 21, 105], [107, 23, 22, 106], [108, 24, 23, 107], [109, 25, 24, 108], [110, 26, 25, 109], [111, 27, 26, 110], [115, 120, 117, 114], [119, 116, 113, 118], [121, 118, 113], [121, 117, 118], [121, 113, 114], [121, 114, 117], [115, 116, 112], [120, 115, 112], [119, 120, 112], [116, 119, 112], [116, 115, 114, 113], [120, 119, 118, 117]]
    
    mesh = bpy.data.meshes.new(name="New Object Mesh")
    mesh.from_pydata(verts, edges, faces)
    # useful for development when the mesh may be invalid.
    # mesh.validate(verbose=True)
    object_data_add(context, mesh, operator=self)


class OBJECT_OT_add_object(Operator, AddObjectHelper):
    """Create a new Mesh Object"""
    bl_idname = "mesh.add_y_axis"
    bl_label = "Add Y Axis Mesh Object"
    bl_options = {'REGISTER', 'UNDO'}

    scale: FloatVectorProperty(
        name="Scale",
        default=(1.0, 1.0, 1.0),
        subtype='TRANSLATION',
        description="scaling",
    )

    def execute(self, context):

        add_object(self, context)

        return {'FINISHED'}


# Registration

def add_object_button(self, context):
    self.layout.operator(
        OBJECT_OT_add_object.bl_idname,
        text="Add Y Axis",
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