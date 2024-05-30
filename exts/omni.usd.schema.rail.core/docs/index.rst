Custom Joint Schema
##################################

Example of custom joint schema. Defines a custom joint as a typed schema, the joint must be deriving from the UsdPhysicsJoint
in order to be recognized as a physics joint.

Build
************************************

The schema definition is defined in a usda file schema definition file:
    - source/extensions/omni.usd.schema.custom.joint/source/schema.usda

Running build process will generate codeless schema for the schema file above, to trigger the schema generate
it is needed to add the location of the schema.usda file into  tools/repoman/build.py (note that this will be removed
from in the future release and it will be part of repo definitions.)

Generating the schema will generate these files:
    - source/extensions/omni.usd.schema.custom.joint/source/generatedSchema.usda -- schema definition file for the USD
    - source/extensions/omni.usd.schema.custom.joint/source/plugInfo.json -- plugin definition file for the USD plugin registry

Extension functionality
************************************

The schema extension makes sure that the generated schema information is plugged into USD.

.. toctree::
    :maxdepth: 1

    README.md
    CHANGELOG.md
