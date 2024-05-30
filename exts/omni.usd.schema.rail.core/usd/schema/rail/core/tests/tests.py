import omni.kit.test
from pxr import Plug, Tf, Usd

class PhysxCustomJointSchemaTests(omni.kit.test.AsyncTestCaseFailOnLogError):
    async def setUp(self):
        pass

    async def tearDown(self):
        pass

    async def test_prim_types(self):
        custom_joint_plugin = Plug.Registry().GetPluginWithName("physxCustomJoint")
        self.assertTrue(custom_joint_plugin != None)

        expected_prim_types = [
            "PhysxCustomJointPhysxPulleyJoint"
        ]

        for prim_type in expected_prim_types:
            ret_val = custom_joint_plugin.DeclaresType(Tf.Type(prim_type))
            self.assertTrue(ret_val)

        reg = Usd.SchemaRegistry()

        typeName = "PhysxPulleyJoint"
        concreteDef = reg.FindConcretePrimDefinition(typeName)

        self.assertTrue(concreteDef)
        self.assertTrue(reg.IsConcrete(typeName))
        self.assertTrue(not reg.IsAppliedAPISchema(typeName))
