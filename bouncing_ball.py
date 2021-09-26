bl_info = {
    "name": "Boucing Ball",
    "author": "James R. Torres",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Boucing Ball",
    "warning": "",
    "doc_url": "",
    "category": "Physics",
}

import bpy
import numpy as np

class BoucingBall(bpy.types.Operator):
    """boucing ball."""

    bl_idname = "object.bouncing"
    bl_label = "Bola Quicando"
    bl_options = {'REGISTER', 'UNDO'}

    radius: bpy.props.FloatProperty(
        name="Raio da Bola",
        description="Define o raio da bola",
        default=0.06,
        min=0.0, soft_max=0.5        
    )

    init_r: bpy.props.FloatVectorProperty(
        name="Posição Inicial",
        description="Define o vetor posição inicial",
        default=(0.0, 0.0, 0.0),
        subtype='XYZ',
        size=3,
        precision=2
    )        
    angle_theta: bpy.props.FloatProperty(
        name="Ângulo Azimutal",
        description="Ângulo azimutal",
        default=0.0,
        min=0.0, soft_max=360,
    )
    angle_phi: bpy.props.FloatProperty(
        name="Ângulo Polar",
        description="Ângulo polar",
        default=45.0,
        min=0, soft_max=180,
    )
    velocity: bpy.props.FloatProperty(
        name="Velocidade Inicial",
        description="Módulo da velocidade inicial",
        default=5.0,
    )
    k_factor: bpy.props.FloatProperty(
        name="Coef. de Atrito",
        description="Coeficiente de atrito",
        default=1.0,
        min=0.0, soft_max=10.0
    )    
    wind: bpy.props.FloatVectorProperty(
        name="Ventos",
        description="Define o vetor velocidade do vento",
        default=(0.0,0.0,0.0),
        subtype='XYZ',
        size=3,
        precision=2
    )
    endtime: bpy.props.FloatProperty(
        name="Tempo Final",
        description="Tempo final",
        #default=2.0,
        min=0.01, soft_max=100,
    )                
    npoints: bpy.props.IntProperty(
        name="Número de Pontos",
        description="Numero de pontos",
        default=500,
        min=2, soft_max=2000,
    )
    floor: bpy.props.FloatProperty(
        name="Piso",
        description="Piso",
        default=0.00
    )
    axisScale: bpy.props.FloatProperty(
        name="Eixos",
        description="Escala dos eixos",
        default=1.00
    )
    axisScale: bpy.props.FloatProperty(
        name="Eixos",
        description="Escala dos eixos",
        default=1.00
    )
    var_bool: bpy.props.BoolProperty(
        name="Linha",
        description="Exibe/oculta a linha",
        default=True
    )
    color: bpy.props.FloatVectorProperty(
        name="Cor da Linha",
        description="Define a cor da linha",
        default=(1.0,0.0,0.0),
        subtype='COLOR',
        size=3,
        min=0.0, soft_max=1.0
    )
    colorball: bpy.props.FloatVectorProperty(
        name="Cor da Bola",
        description="Define a cor da bola",
        default=(1.0,1.0,1.0,1.0),
        subtype='COLOR',
        size=4,
        min=0.0, soft_max=1.0
    )              

    hidexyz: bpy.props.BoolVectorProperty(
        name="Esconder os Eixos",
        description="Esconde os eixos",
        default=(False, False, False),
        subtype='XYZ',
        size=3,
    )
    
    path: bpy.props.StringProperty(
        name="Salvar Vídeo",
        description="Digite o caminho",
        default="/home/james/Vídeos/teste.avi",
    )
        
    formato: bpy.props.StringProperty(
        name="Formato",
        description="PNG; FFmpeg",
        default="FFMPEG",
    )
    
    framestart: bpy.props.FloatProperty(
        name="Quadro Inicial",
        description="Define o quadro inicial",
        default=0.0,
        min=0.0, soft_max=1000.0          
    )
    frameend: bpy.props.FloatProperty(
        name="Quadro Final",
        description="Define o quadro final",
        default=500.0,
        min=0.0, soft_max=1000.0        
    )    

    framerate: bpy.props.FloatProperty(
        name="Taxa de quadros",
        description="Taxa de quadros por segundo",
        default=250.0
    )    
    
    render: bpy.props.BoolProperty(
        name="Renderizar",
        description="Gera um vídeo",
        default=False
    )
    
    overlapping: bpy.props.BoolProperty(
        name="Sobrepor Simulação",
        description="Simulação sobrepostas ",
        default=False
    )
    
    diagonal: bpy.props.FloatProperty(
        name="Vetor",
        description="Comprimento do vetor",
        default=0.5,
        min=0.0, soft_max=2.0
    )

    boolvec: bpy.props.BoolProperty(
        name="Mostrar Vetores",
        description="Mostra os vetores velocidade",
        default=False
    )
    boolboxvec: bpy.props.BoolProperty(
        name="Mostrar Box",
        description="Mostra a regra do paralelogramo",
        default=False
    )
    dist: bpy.props.BoolProperty(
        name="Mostrar Distâncias",
        description="Mostra a distância da bola à origem e a altura da bola",
        default=False
    )        
    anotation: bpy.props.BoolProperty(
        name="Mostrar Anotações",
        description="Mostra anotações diversas",
        default=True
    )
                                            

    def execute(self, context):     
        """."""

        bpy.context.space_data.shading.type = 'MATERIAL'
        bpy.context.space_data.overlay.show_cursor = False


        bpy.data.scenes["Scene"].measureit_gl_ghost=self.anotation

        def select(objName):
            bpy.ops.object.select_all(action='DESELECT')
            bpy.data.objects[objName].select_set(True)

        def activate(objName):
            bpy.context.view_layer.objects.active = bpy.data.objects[objName]

        if self.overlapping == False:
            bpy.ops.object.select_all(action='SELECT')
            bpy.ops.object.delete(use_global=False, confirm=False)        
        else:
            objs = [ob for ob in bpy.context.scene.objects if ob.name in ('eixoX', 'eixoY', 'eixoZ')]
            bpy.ops.object.delete({"selected_objects": objs})
            bpy.ops.object.delete({"selected_objects": objs})
        # criando o eixo x
        bpy.ops.mesh.add_x_axis(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0),
         scale=(self.axisScale, self.axisScale, self.axisScale))
        bpy.context.object.name = 'eixoX'
        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes =True
        bpy.context.object.active_material = material_basic
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = (1, 0 , 0, 1)

        # criando o eixo y                
        bpy.ops.mesh.add_y_axis(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0),
         scale=(self.axisScale, self.axisScale, self.axisScale))
        bpy.context.active_object.name = 'eixoY'          
        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes =True
        bpy.context.object.active_material = material_basic
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = (0, 1 , 0, 1)

        # criando o eixo z              
        bpy.ops.mesh.add_z_axis(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0),
         scale=(self.axisScale, self.axisScale, self.axisScale))
        bpy.context.active_object.name = 'eixoZ'          
        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes =True
        bpy.context.object.active_material = material_basic
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = (0, 0 , 1, 1)         
              
              
        # criando vetor e arrows
        lamb=self.diagonal
        bpy.ops.mesh.add_base(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), scale=(lamb/2, lamb/2, lamb/2))
        bpy.context.object.name = "arrows_vel"
        if self.boolvec == True:
            bpy.context.object.hide_viewport = False  
        else:
            bpy.context.object.hide_viewport = True
            bpy.context.object.show_bounds=True

        if self.boolboxvec == True:
            bpy.context.object.hide_viewport = False
            bpy.context.object.show_bounds = True
        else:
            pass
        bpy.context.editable_objects

        # criando circulo   
        bpy.ops.object.empty_add(type='CIRCLE', align='WORLD', location=(0, 0, 0), rotation=(1.5708, 0, 0), scale=(1, 1, 1))
        bpy.context.object.name = "circulo"
        bpy.data.objects['circulo'].scale=(self.radius, self.radius, self.radius)

        # criando a bola
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=1, enter_editmode=False, align='WORLD',
            location=(0, 0, 0), scale=(self.radius, self.radius, self.radius)
            )
        bpy.context.object.name = "bola"   
        bpy.ops.object.shade_smooth(True)
        if self.dist == True:
            bpy.ops.measureit.addorigin()
        else:
            pass

        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes =True
        bpy.context.object.active_material = material_basic
        principled_node = material_basic.node_tree.nodes.get('Principled BSDF')
        principled_node.inputs[0].default_value = self.colorball

        bpy.data.objects["bola"].select_set(True)
        bpy.data.objects["circulo"].select_set(True)        
        context.view_layer.objects.active = bpy.data.objects["bola"]
        if self.dist == True:
            bpy.ops.measureit.addlink()
        else:
            pass        
        bpy.data.objects["circulo"].select_set(False)  

        # discretizacao
        positions = []
        velocity = []
    
        a = 0.0
        b = 0.00001 + self.endtime
        N = self.npoints
        h = float((b - a)/(N - 1))
        frame_rate = self.npoints/(b - a)
        bpy.data.scenes["Scene"].render.fps=self.framerate
        print(frame_rate)
        # condicoes inicias

        # angulos em graus
        theta = self.angle_theta   #azimutal
        phi = 90 - self.angle_phi  #polar
        # angulos em radianos
        theta = theta*np.pi/180
        phi = phi*np.pi/180

        v0 = self.velocity

        cos_theta = np.cos(theta)
        sin_theta = np.sin(theta)
        cos_phi = np.cos(phi)
        sin_phi = np.sin(phi)

        x0, y0, z0 = self.init_r
        vx0, vy0, vz0 = v0*cos_theta*sin_phi, v0*sin_theta*sin_phi, v0*cos_phi
        ux, uy, uz = self.wind
          
        # constantes
        g = 9.86
        k = self.k_factor
        solo = self.floor
        def fx(t):
            return vx

        def fy(t):
            return vy

        def fz(t):
            return vz

        def gx(t, x, y, z):
            return k*(ux - vx)

        def gy(t, x, y, z):
            return k*(uy - vy)

        def gz(t, x, y, z):
            return - g + k*(uz - vz)

        # main loop
        x, y, z = x0, y0, z0
        vx, vy, vz = vx0, vy0, vz0

        for i in range(N):
            t = a + i*h
            k1_fx = fx(t)
            k2_fx = fx(t + h/2)
            k3_fx = fx(t + h/2)
            k4_fx = fx(t + h)
            x = x + (k1_fx + 2*k2_fx + 2*k3_fx + k4_fx)*h/6

            k1_fy = fy(t)
            k2_fy = fy(t + h/2)
            k3_fy = fy(t + h/2)
            k4_fy = fy(t + h)
            y = y + (k1_fy + 2*k2_fy + 2*k3_fy + k4_fy)*h/6

            k1_fz = fz(t)
            k2_fz = fz(t + h/2)
            k3_fz = fz(t + h/2)
            k4_fz = fz(t + h)
            z = z + (k1_fz + 2*k2_fz + 2*k3_fz + k4_fz)*h/6

            k1_gx = gx(t, x, y, z)
            k2_gx = gx(t + h/2, x + h/2*k1_gx, y + h/2*k1_gx, z + h/2*k1_gx)
            k3_gx = gx(t + h/2, x + h/2*k2_gx, y + h/2*k2_gx, z + h/2*k2_gx)
            k4_gx = gx(t + h, x + h*k3_gx, y + h*k3_gx, z + h*k3_gx)
            vx = vx + (k1_gx + 2*k2_gx + 2*k3_gx + k4_gx)*h/6

            k1_gy = gy(t, x, y, z)
            k2_gy = gy(t + h/2, x + h/2*k1_gy, y + h/2*k1_gy, z + h/2*k1_gy)
            k3_gy = gy(t + h/2, x + h/2*k2_gy, y + h/2*k2_gy, z + h/2*k2_gy)
            k4_gy = gy(t + h, x + h*k3_gy, y + h*k3_gy, z + h*k3_gy)
            vy = vy + (k1_gy + 2*k2_gy + 2*k3_gy + k4_gy)*h/6

            k1_gz = gz(t, x, y, z)
            k2_gz = gz(t + h/2, x + h/2*k1_gz, y + h/2*k1_gz, z + h/2*k1_gz)
            k3_gz = gz(t + h/2, x + h/2*k2_gz, y + h/2*k2_gz, z + h/2*k2_gz)
            k4_gz = gz(t + h, x + h*k3_gz, y + h*k3_gz, z + h*k3_gz)
            
            if z >= solo:
                vz = vz + (k1_gz + 2*k2_gz + 2*k3_gz + k4_gz)*h**1/6
                positions.append([x, y, z])
                velocity.append([vx, vy, vz])
            else:
                vz = vz + (k1_gz + 2*k2_gz + 2*k3_gz + k4_gz)*h**1/6
                vz = - vz
                positions.append([x, y, z])
                velocity.append([vx, -vy, vz])
            
                continue
                # start_pos = (z0, y0, z0)
        obja = bpy.data.objects["bola"]
        objb = bpy.data.objects["arrows_vel"]
        objd = bpy.data.objects["circulo"]                               
        frame_num = 0
        for position in positions:
            bpy.context.scene.frame_set(frame_num)
            obja.location = position
            obja.keyframe_insert(data_path="location", index=-1)
            objb.location = position
            objb.keyframe_insert(data_path="location", index=-1)        
            objd.location = [position[0], position[1],0.0]                                   
            objd.keyframe_insert(data_path="location", index=-1)                
            frame_num += 1
        frame_num = 0            
        for scale in velocity:
            bpy.context.scene.frame_set(frame_num)
            objb.scale = [scale[0]*lamb, scale[1]*lamb, scale[2]*lamb] 
            objb.keyframe_insert(data_path="scale", index=-1)             
            frame_num += 1                       
        bpy.ops.object.paths_calculate(start_frame=1, end_frame=N)
        bpy.context.object.motion_path.use_custom_color=True       
        bpy.context.object.motion_path.lines=True     
        bpy.context.object.motion_path.color=self.color
        bpy.context.object.motion_path.line_thickness=1.0
        bpy.context.object.animation_visualization.motion_path.show_keyframe_numbers=True     
        bpy.context.object.animation_visualization.motion_path.show_keyframe_highlight=False      
        bpy.ops.object.paths_update()
        bpy.ops.object.select_all(action='DESELECT')
        if self.var_bool == False:
            bpy.ops.object.paths_clear()
        else:
            pass
        bpy.data.objects["eixoX"].hide_viewport=self.hidexyz[0]
        bpy.data.objects["eixoY"].hide_viewport=self.hidexyz[1]
        bpy.data.objects["eixoZ"].hide_viewport=self.hidexyz[2]
        bpy.data.scenes["Scene"].render.filepath=self.path
        bpy.data.scenes["Scene"].render.image_settings.file_format=self.formato
        bpy.data.scenes["Scene"].frame_start=self.framestart
        bpy.data.scenes["Scene"].frame_end=self.frameend
        bpy.ops.render.opengl(animation=self.render)
        return {'FINISHED'}


class VIEW3D_PT_bouncing_ball(bpy.types.Panel):
    """."""

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Simulação Física'
    bl_label = ''

    def draw_header(self, context):
        """."""
        layout = self.layout
        layout.label(text="Lançamento de Projétil")
        
    def draw(self, context):
        """."""
        self.layout.operator('object.bouncing',
                             text='Simular', icon='SHADING_RENDERED')
        self.layout.operator('object.select_all',
                             text='Selecionar', icon='BORDERMOVE') 
        self.layout.operator('object.delete',
                             text='Limipar Tudo', icon='BRUSH_DATA')                                                         
        self.layout.operator('object.bouncing',
                             text='Painel', icon='MENU_PANEL')
        self.layout.operator( "measureit.runopengl" ,
                             text='Réguas', icon='DRIVER_DISTANCE')                                                                                                           
        props = self.layout.operator('object.bouncing', text='Default',
                                     icon='IPO_ELASTIC')
                                       
                                                                                                                            
        props.radius = 0.06
        props.init_r = (0.0, 0.0, 0.0)
        props.k_factor = 1.0
        props.angle_theta = 0
        props.angle_phi = 45
        props.velocity = 5.0
        props.wind = (0.0, 0.0, 0.0)
        props.endtime = 5.0        
        props.npoints = 500
        props.floor = 0.0
        props.axisScale = 1.0
        props.color=(1.0, 0.0, 0.0)


def register():
    """Hallo."""
    bpy.utils.register_class(BoucingBall)
    bpy.utils.register_class(VIEW3D_PT_bouncing_ball)


def unregister():
    """Goodby."""
    bpy.utils.unregister_class(BoucingBall)
    bpy.utils.unregister_class(VIEW3D_PT_bouncing_ball)


if __name__ == "__main__":
    register()
