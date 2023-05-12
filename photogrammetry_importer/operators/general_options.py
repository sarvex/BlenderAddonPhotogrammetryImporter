import os
import sys
import bpy
from bpy.props import BoolProperty
from photogrammetry_importer.blender_utility.logging_utility import log_report


class GeneralOptions:
    """Class to define and apply general options."""

    adjust_clipping_distance: BoolProperty(
        name="Adjust Clipping Distance",
        description="Adjust clipping distance of 3D view.",
        default=False,
    )

    def draw_general_options(self, layout):
        """Draw general options."""
        mesh_box = layout.box()
        mesh_box.prop(self, "adjust_clipping_distance")

    def apply_general_options(self):
        """Apply the options defined by this class."""
        if not self.adjust_clipping_distance:
            return
        log_report(
            "INFO", "Adjust clipping distance of 3D view: ...", self
        )
        active_space = next(
            (
                area.spaces.active
                for area in bpy.context.screen.areas
                if area.type == "VIEW_3D"
            ),
            None,
        )
            # Setting "active_space.clip_end" to values close to "sys.maxsize"
            # causes strange graphical artifacts in the 3D view.
        active_space.clip_end = (
            2**55 - 1 if sys.maxsize == 2**63 - 1 else 2**23 - 1
        )
        log_report(
            "INFO", "Adjust clipping distance of 3D view: Done", self
        )
