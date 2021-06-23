# <pep8-80 compliant>
# 234567890123456789012345678901234567890123456789012345678901234567890123456789
# 23456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF
from . import new


def camera(name):
    return new.object(name, new.camera(name))


class image():  # incomplete
    @classmethod
    def register(cls):
        cls.data = bpy.data.images

    @staticmethod
    def new(name, width, height):
        return bpy.data.images.new(name, width, height)

    @staticmethod
    def load(name, width, height):
        return bpy.data.images.load(filepath, check_existing)
#    return bpy.data.images.load(filepath, check_existing=check_existing)


class light():
    @staticmethod
    def area(name):
        return new.object(name, new.light.area(name))

    @staticmethod
    def point(name):
        return new.object(name, new.light.point(name))

    @staticmethod
    def spot(name):
        return new.object(name, new.light.spot(name))

    @staticmethod
    def sun(name):
        return new.object(name, new.light.sun(name))


class mesh():  # invalid data
    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)


class mesh():  # not valid
    @classmethod
    def register(cls):
        cls.data = bpy.data.meshes

    def mesh(name, vertices, edges, faces):
        mesh = data(bpy.data.meshes, name)
        mesh.from_pydata(vertices, edges, faces)
        return empty_object(name, mesh)

