import omni.ext
import omni.usd
from pxr import Tf
from omni.kit.property.physx import register_schema, unregister_schema
from omni.physxui import PhysicsMenu
from omni.usd.commands.usd_commands import DeletePrimsCommand
from omni.kit.commands import Command, register_all_commands_in_module, execute


# minimal implementation of a type class for a codeless schema to work with physics widgets
class PhysicsTrackJointCls(Tf.Type):
    __name__ = "PhysicsTrackJoint"

    def __init__(self):
        super().__init__("UsdPhysicsTrackJoint")

PhysicsTrackJoint = PhysicsTrackJointCls()

class PhysicsTractionForceCharacteristicCls(Tf.Type):
    __name__ = "PhysicsTractionForceCharacteristic"

    def __init__(self):
        super().__init__("UsdPhysicsTractionForceCharacteristic")

PhysicsTractionForceCharacteristic = PhysicsTractionForceCharacteristicCls()

class PhysicsWheelFrameCls(Tf.Type):
    __name__ = "PhysicsWheelFrame"

    def __init__(self):
        super().__init__("UsdPhysicsWheelFrame")

PhysicsWheelFrame = PhysicsWheelFrameCls()

class PhysicsWheelsetCls(Tf.Type):
    __name__ = "PhysicsWheelset"

    def __init__(self):
        super().__init__("UsdPhysicsWheelset")

PhysicsWheelset = PhysicsWheelsetCls()

class TS1SlipSwitchCls(Tf.Type):
    __name__ = "TS1SlipSwitch"

    def __init__(self):
        super().__init__("UsdTS1SlipSwitch")

TS1SlipSwitch = TS1SlipSwitchCls()

class TS2SlipSwitchCls(Tf.Type):
    __name__ = "TS2SlipSwitch"

    def __init__(self):
        super().__init__("UsdTS2SlipSwitch")

TS2SlipSwitch = TS2SlipSwitchCls()

class TS2WaySwitchCls(Tf.Type):
    __name__ = "TS2WaySwitch"

    def __init__(self):
        super().__init__("UsdTS2WaySwitch")

TS2WaySwitch = TS2WaySwitchCls()

class TS3WaySwitchCls(Tf.Type):
    __name__ = "TS3WaySwitch"

    def __init__(self):
        super().__init__("UsdTS3WaySwitch")

TS3WaySwitch = TS3WaySwitchCls()

class TSTrackSystemCls(Tf.Type):
    __name__ = "TSTrackSystem"

    def __init__(self):
        super().__init__("UsdTSTrackSystem")

TSTrackSystem = TSTrackSystemCls()

class TSTrackCollectionCls(Tf.Type):
    __name__ = "TSTrackCollection"

    def __init__(self):
        super().__init__("UsdTSTrackCollection")

TSTrackCollection = TSTrackCollectionCls()

class TSTrackCls(Tf.Type):
    __name__ = "TSTrack"

    def __init__(self):
        super().__init__("UsdTSTrack")

TSTrack = TSTrackCls()


# basic command (undoable primitive) to add a custom joint to stage
# finds first free path and selects the prim afterwards
class PhysicsTrackJointAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/TrackJoint", True)
            stage.DefinePrim(self._path, "PhysicsTrackJoint")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class PhysicsTractionForceCharacteristicAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/TractionForceCharacteristic", True)
            stage.DefinePrim(self._path, "PhysicsTractionForceCharacteristic")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class PhysicsWheelFrameAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/WheelFrame", True)
            stage.DefinePrim(self._path, "PhysicsWheelFrame")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class PhysicsWheelsetAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/Wheelset", True)
            stage.DefinePrim(self._path, "PhysicsWheelset")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TS1SlipSwitchAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/SingleSlipSwitch", True)
            stage.DefinePrim(self._path, "TS1SlipSwitch")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TS2SlipSwitchAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/DoubleSlipSwitch", True)
            stage.DefinePrim(self._path, "TS2SlipSwitch")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TS2WaySwitchAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/TwoWaySwitch", True)
            stage.DefinePrim(self._path, "TS2WaySwitch")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TS3WaySwitchAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/ThreeWaySwitch", True)
            stage.DefinePrim(self._path, "TS3WaySwitch")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TSTrackSystemAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/TrackSystem", True)
            stage.DefinePrim(self._path, "TSTrackSystem")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TSTrackCollectionAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/TrackCollection", True)
            stage.DefinePrim(self._path, "TSTrackCollection")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()

class TSTrackAddCommand(Command):
    def do(self):
        context = omni.usd.get_context()
        stage = context.get_stage()
        if stage:
            self._path = omni.usd.get_stage_next_free_path(stage, "/Track", True)
            stage.DefinePrim(self._path, "TSTrack")
            context.get_selection().set_selected_prim_paths([self._path], True)
        else:
            self._path = None

    def undo(self):
        if self._path is not None:
            DeletePrimsCommand([self._path]).do()


class PhysxCustomJointExtension(omni.ext.IExt):
    def on_startup(self):
        # registering the schema will enable the Track Joint widget in the Property window
        register_schema(PhysicsTrackJoint)
        register_schema(PhysicsTractionForceCharacteristic)
        register_schema(PhysicsWheelFrame)
        register_schema(PhysicsWheelset)
        register_schema(TSTrackSystem)
        register_schema(TSTrackCollection)
        register_schema(TSTrack)
        register_schema(TS1SlipSwitch)
        register_schema(TS2SlipSwitch)
        register_schema(TS2WaySwitch)
        register_schema(TS3WaySwitch)

        # add a menu item to the "Create" section of main menu and viewport and the stage widget popup menus
        self._menu_item1 = {
            "name": "rail: Trackjoint",
            "onclick_fn": lambda *_: execute("PhysicsTrackJointAdd")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item1)

        self._menu_item2 = {
            "name": "rail: Traction Force Characteristic",
            "onclick_fn": lambda *_: execute("PhysicsTractionForceCharacteristicAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item2)

        self._menu_item3 = {
            "name": "rail: Wheelframe",
            "onclick_fn": lambda *_: execute("PhysicsWheelFrameAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item3)
      
        self._menu_item4 = {
            "name": "rail: Wheelset",
            "onclick_fn": lambda *_: execute("PhysicsWheelsetAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item4)

        self._menu_item5 = {
            "name": "rail: Track System",
            "onclick_fn": lambda *_: execute("TSTrackSystemAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item5)

        self._menu_item6 = {
            "name": "raile: Track Collection",
            "onclick_fn": lambda *_: execute("TSTrackCollectionAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item6)

        self._menu_item7 = {
            "name": "rail: Track",
            "onclick_fn": lambda *_: execute("TSTrackAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item7)

        self._menu_item8 = {
            "name": "rail: Two Way Switch",
            "onclick_fn": lambda *_: execute("TS2WaySwitchAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item8)

        self._menu_item9 = {
            "name": "rail: Three Way Switch",
            "onclick_fn": lambda *_: execute("TS3WaySwitchAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item9)

        self._menu_item10 = {
            "name": "rail: Single Slip Switch",
            "onclick_fn": lambda *_: execute("TS1SlipSwitchAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item10)

        self._menu_item11 = {
            "name": "rail: Double Slip Switch",
            "onclick_fn": lambda *_: execute("TS2SlipSwitchAddCommand")
        }
        PhysicsMenu.add_context_menu("Create", self._menu_item11)


    def on_shutdown(self):
        unregister_schema(TS1SlipSwitch)
        unregister_schema(TS2SlipSwitch)
        unregister_schema(TS2WaySwitch)
        unregister_schema(TS3WaySwitch)
        unregister_schema(TSTrack)
        unregister_schema(TSTrackCollection)
        unregister_schema(TSTrackSystem)
        unregister_schema(PhysicsWheelset)
        unregister_schema(PhysicsWheelFrame)
        unregister_schema(PhysicsTractionForceCharacteristic)
        unregister_schema(PhysicsTrackJoint)
        PhysicsMenu.remove_context_menu("Create", self._menu_item7)
        PhysicsMenu.remove_context_menu("Create", self._menu_item6)
        PhysicsMenu.remove_context_menu("Create", self._menu_item5)
        PhysicsMenu.remove_context_menu("Create", self._menu_item4)
        PhysicsMenu.remove_context_menu("Create", self._menu_item3)
        PhysicsMenu.remove_context_menu("Create", self._menu_item2)
        PhysicsMenu.remove_context_menu("Create", self._menu_item1)


register_all_commands_in_module(__name__)