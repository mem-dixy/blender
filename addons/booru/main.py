# <pep8-80 compliant>
import bpy  # pylint: disable=import-error

from blender import data
from blender import mesh
from booru import preferences
from blender import UV


ready = False
Image_Formats = [
    ".bmp",
    ".sgi",
    ".rgb",
    ".bw",
    ".png",
    ".jpg",
    ".jpeg",
    ".jp2",
    ".j2c",
    ".tga",
    ".cin",
    ".dpx",
    ".exr",
    ".hdr",
    ".tif",
    ".tiff",
    ".webp",
]


class BOORU_mesh_make(bpy.types.Operator):
    bl_label = "Plane"
    bl_idname = "blenderbooru.mesh_make"

    def __init__(self):
        self.spot = 0

    def _new_object(self, context, image):
        mush = mesh.image(image)
        box = data.mesh.make("image", mush)
        box.location = (self.spot, 0, 0)
        self.spot += 2.5
        return box

    def execute(self, context):
        print("start")
        self.spot = 0
        from .plugin import OS
        content = preferences.content()
        (path, file) = OS.walk_directory(content.root)
        images = []
        for (filenames) in file:
            (dirpath, name) = filenames
            ext = OS.file_extension(name).lower()
            if ext in Image_Formats:
                merge = OS.join(dirpath, name)
                images.append(merge)
        for file in images:
            print("convert " + file)
            image = data.image.load(file)
            material = UV.material("pretty", image)
            object = self._new_object(context, image)
            object.data.materials.append(material)
        print("done")
        return {'FINISHED'}


class BOORU_mesh_delete(bpy.types.Operator):
    bl_label = "Delete Me Now"
    bl_idname = "blenderbooru.mesh_delete"

    def execute(self, context):
        # currently selected at the momnet
        object = bpy.context.object
        if object:
            # what about the other materials?
            if object.active_material:
                data.material.remove(object.active_material)
            data.object.remove(object)
        return {'FINISHED'}


class BOORU_clear_all(bpy.types.Operator):
    bl_label = "Clear all data"
    bl_idname = "blenderbooru.clear_all"

    def execute(self, context):
        # this probably highly unoptimized.
        # try doing this backwarks
        for camera in bpy.data.cameras:
            data.camera.remove(camera)
        for light in bpy.data.lights:
            data.light.remove(light)
        for material in bpy.data.materials:
            data.material.remove(material)
        for mesh in bpy.data.meshes:
            data.mesh.remove(mesh)
        for image in bpy.data.images:
            data.image.remove(image)
        for texture in bpy.data.textures:
            data.texture.remove(texture)
        light = data.light.sun.make("lili")
        light.location = (0, 0, 1)
        camera = data.camera.make("cool cat")
        camera.location = (0, 0, 10)
        return {'FINISHED'}


class BOORU_checkers(bpy.types.Operator):
    bl_label = "Spawn Checkers"
    bl_idname = "blenderbooru.checkers"

    def _red(self, x, y, z):
        mush = data.all_stuff.object_("red", mesh.plane())
        mush.location = (x, y, z)
        return mush

    def _green(self, x, y, z):
        mush = data.all_stuff.object_("green", mesh.plane())
        mush.location = (x, y, z)
        return mush

    def execute(self, context):
        self._red(0, 0, 0)
        self._green(0, 10, 0)
        self._red(0, 0, 10)
        return {'FINISHED'}


class BOORU_main(bpy.types.Panel):
    bl_category = "Tab Name"
    bl_context = ""
    bl_idname = "BOORU_PT_main_panel2"
    bl_label = "Main Panel"
    bl_options = {'DEFAULT_CLOSED'}
    bl_order = 0
    bl_owner_id = ""
    bl_parent_id = ""
    bl_region_type = 'UI'
    bl_space_type = 'VIEW_3D'
    bl_translation_context = "*"
    bl_ui_units_x = 0

    bl_label = "Select a TAG"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    #bl_context = 'object'
    # bl_context = "OBJECT"
    bl_options = {'DEFAULT_CLOSED'}
    ###
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "bbb"
    bl_label = "Landmarks yay"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        global ready
        if not ready:
            self.layout.operator("blenderbooru.register")
        else:
            self.layout.operator("blenderbooru.unregister")
            #
            self.layout.label(text="Hello World")
            self.layout.operator("blenderbooru.mesh_make")
            self.layout.operator("blenderbooru.mesh_delete")
            self.layout.operator("blenderbooru.clear_all")
            self.layout.operator("blenderbooru.checkers")
            #
            content = preferences.content()
            self.layout.prop(content, "boolean")
            if content.boolean:
                self.layout.label(text="checkbox is on")
            else:
                self.layout.label(text="checkbox is off")


class BOORU_register(bpy.types.Operator):
    bl_label = "Startup"
    bl_idname = "blenderbooru.register"

    def execute(self, context):
        global ready
        data.register()
        ready = True
        return {'FINISHED'}


class BOORU_unregister(bpy.types.Operator):
    bl_label = "Shutdown"
    bl_idname = "blenderbooru.unregister"

    def execute(self, context):
        global ready
        data.unregister()
        ready = False
        return {'FINISHED'}


def register():
    bpy.utils.register_class(BOORU_main)
    bpy.utils.register_class(BOORU_mesh_make)
    bpy.utils.register_class(BOORU_mesh_delete)
    bpy.utils.register_class(BOORU_clear_all)
    bpy.utils.register_class(BOORU_checkers)
    #
    bpy.utils.register_class(BOORU_unregister)
    bpy.utils.register_class(BOORU_register)


def unregister():
    bpy.utils.unregister_class(BOORU_checkers)
    bpy.utils.unregister_class(BOORU_mesh_delete)
    bpy.utils.unregister_class(BOORU_mesh_make)
    bpy.utils.unregister_class(BOORU_clear_all)
    bpy.utils.unregister_class(BOORU_main)
    #
    bpy.utils.unregister_class(BOORU_register)
    bpy.utils.unregister_class(BOORU_unregister)