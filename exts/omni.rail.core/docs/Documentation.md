# Reference


## PhysicsTrackJoint

A custom joint for the PhysX engine that keeps a 
wheel frame on a track.

   \          | PhysicsTrackJoint
------------- | ----------------------------
Inherits:     | PhysicsJoint


### Body 0

Relationship to any UsdGeomXformable.

   \          | physics:body0
------------- | ----------------------------
Type:         | Relationship


### Break Force

Joint break force. If set, joint is to break when 
this force limit is reached. (Used for linear dofs.) 

   \          | physics:breakForce
------------- | ----------------------------
Type:         | float
Dimension:    | mass * distance / time / time
Units:        | inherited from mass, distance, time
Range:        | [0,inf]
Default Value:| inf


### Break Torque

Joint break torque. If set, joint is to break when this torque 
limit is reached. (Used for angular dofs.) 

   \          | physics:breakTorque
------------- | ----------------------------
Type:         | float
Dimension:    | mass * distance * distance / time / time
Units:        | inherited from mass, distance, time
Range:        | [0,inf]
Default Value:| inf


### Collision Enabled

Determines if the jointed subtrees should collide or not.

   \          | physics:collisionEnabled
------------- | ----------------------------
Type:         | bool
Dimension:    | One
Range:        | 0,1
Default Value:| 0


### Exclude From Articulation

Determines if the joint can be included in an Articulation.

   \          | physics:excludeFromArticulation
------------- | ----------------------------
Type:         | bool
Dimension:    | One
Range:        | 0,1
Default Value:| 0


### Joint Enabled

Determines if the joint is enabled.

   \          | physics:jointEnabled
------------- | ----------------------------
Type:         | bool
Dimension:    | One
Range:        | 0,1
Default Value:| 1


### Local Position 0

Relative position of the joint frame to body0's frame.

   \          | physics:localPos0
------------- | ----------------------------
Type:         | point3f
Dimension:    | distance
Default Units:| inherited
Range:        | ]-inf,+inf[
Default Value:| (0, 0, 0)


### Local Rotation 0

Relative orientation of the joint frame to body0's frame.

   \          | physics:localRot0
------------- | ----------------------------
Type:         | quatf
Dimension:    | 
Default Units:| 
Range:        | 
Default Value:| (1, 0, 0, 0)


### Force Limit Normal Min

Minimum force to be applied along the direction orthogonal to the track. 
Overrides physics:breakForce if authored.

   \          | physics:normalForceLimitsMin
------------- | ----------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [-inf,0kN]
Default Value:| -inf


### Force Limit Normal Max

Maximum force to be applied along the direction orthogonal to the track. 
Overrides physics:breakForce if authored.

   \          | physics:normalForceLimitsMax
------------- | ----------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [0kN,+inf]
Default Value:| +inf


### Torque Limit along Normal

Maximum torque to be applied along the direction orthogonal to 
the track. Overrides physics:breakTorque if authored.

   \          | physics:normalTorqueLimit
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance * distance / time / time
Default Units:| kNm
Range:        | [0kNm,+inf]
Default Value:| +inf


### Force Limit Binormal Min

Minimum force to be applied along the direction perpendicular 
to the track. Overrides physics:breakForce if authored.

   \          | physics:binormalForceLimitsMin
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [-inf,0kN]
Default Value:| 0kN


### Force Limit Binormal Max

Maximum force to be applied along the direction perpendicular 
to the track. Overrides physics:breakForce if authored.

   \          | physics:binormalForceLimitsMax
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [0kN,+inf]
Default Value:| +inf


### Torque Limit along Tangent and Binormal

Maximum torque to be applied along the direction along as well 
as perpendicular to the track. Overrides physics:breakForce 
if authored.

   \          | physics:torqueLimit
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance * distance / time / time
Default Units:| kNm
Range:        | [0kNm,+inf]
Default Value:| +inf


### Force Limit Motor Min

Minimum and maximum force to be applied by the motor to reach 
the target velocity.

   \          | physics:motorForceLimitsMin
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [-inf,0kN]
Default Value:| 0kN


### Force Limit Motor Max

Minimum and maximum force to be applied by the motor to reach 
the target velocity.

   \          | physics:motorForceLimitsMax
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance / time / time
Default Units:| kN
Range:        | [0kN,+inf]
Default Value:| 0kN


### Target Velocity

The target velocity along the track a motor aims for.

   \          | physics:motorTargetVelocity
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance / time
Default Units:| km/h
Range:        | [-inf,+inf]
Default Value:| 0m/s


### Threshold for Position

A positional error in the alignemt of the anchor to 
the track that would lead to derailment.

   \          | physics:thresholdPosition
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance
Default Units:| m
Range:        | ]0m,+inf]
Default Value:| 35cm


### Threshold for Tangent

A rotational error in the alignemt of the anchor to 
the track that would lead to derailment.

   \          | physics:thresholdTangent
------------- | -------------------------
Type:         | float
Dimension:    | One
Units:        | degree
Range:        | ]0,90]
Default Value:| 45


### Threshold for Normal

A rotational error in the alignemt of the anchor to
the track that would lead to derailment.

   \          | physics:thresholdNormal
------------- | -------------------------
Type:         | float
Dimension:    | One
Units:        | degree
Range:        | ]0,90]
Default Value:| 45


### Threshold for Binormal

A rotational error in the alignemt of the anchor to 
the track that would lead to derailment.

   \          | physics:thresholdBinormal
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | One
Units:        | degree
Range:        | ]0,90]
Default Value:| 45


### Flange

The hight of the wheels flange, if any.

   \          | physics:flange
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance
Default Units:| m
Range:        | [0m,+inf]
Default Value:| +inf


### Track System

Reference to a track system to rail the trackjoint on. A track 
system is a prim that contains any 'TSTrack' prims.

   \          | physics:trackSystem
------------- | -------------------------
Type:         | Relationship


## PhysicsTractionForceCharacteristic

Function that defines the characteristic behaviour of a 
engine-gear unit to change its maximum available traction 
force with velocity.

   \          | PhysicsTractionForceCharacteristic
------------- | ----------------------------
Inherits:     | Typed


### Speed Steps

List of speed steps in the charactersitic.

   \          | physics:speedSteps
------------- | -------------------------
Type:         | float2[]
Dimension:    | (distance / time, One)
Units:        | (cm/s,1)
Range:        | ([0,+inf], [0,1])


## PhysicsWheelFrame

A wheel frame holds a track joint and wheesets - makes up a model 
for friction, brake and motor. Add a PhysicsTrackJoint as child 
prim in order to establish a connection to a track system. Add some 
PhysicsWheelset as child prim to  define the maximum drive, braking 
and friction forces, the track joint can apply. A 
PhysicsTractionForceCharacteristic helps to shape a model of the 
engine-gear unit of a rolling stock.

   \          | PhysicsWheelFrame
------------- | ----------------------------
Inherits:     | Typed


### Brake

Sets the fraction of the maximum braking to apply in order 
to reach a zero velocity.

   \          | physics:brake
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | One
Range:        | [0,1]
Default Value:| 0


### Target Velocity

The target velocity along the track a motor aims for.

   \          | physics:targetVelocity
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance / time
Default Units:| km/h
Range:        | [-inf,+inf]
Default Value:| 0m/s


### Thrust

Sets the fraction of the maximum thrust to apply in order to 
reach the target velocity specified by TargetVelocity().

   \          | physics:thrust
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | One
Range:        | [0,1]
Default Value:| 0


### Traction Force Characteristic

Reference to a PhysicsTractionForceCharacteristic.

   \          | physics:tractionForceCharacteristic
------------- | -------------------------
Type:         | Relationship


## PhysicsWheelset

A wheelset is an axle with two wheels attached to it. 
The PhysicsWheelset child prim adds to it's parent's 
PhysicsWheelFrame motor forces.

   \          | PhysicsWheelset
------------- | ----------------------------
Inherits:     | Typed


### Friction Torque

Friction that is introduced by this wheel.

   \          | physics:frictionTorque
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance * distance / time / time
Default Units:| kNm
Range:        | [0kNm,+inf]
Default Value:| 0kNm


### Maximum Braking Torque

Maximum braking torque that this wheelset can apply.

   \          | physics:maxBrakingTorque
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance * distance / time / time
Default Units:| kNm
Range:        | [0kNm,+inf]
Default Value:| 0kNm


### Maximum Motor Torque

Maximum torque that this wheelset can apply for acceleration.

   \          | physics:maxMotorTorque
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | mass * distance * distance / time / time
Default Units:| kNm
Range:        | [0kNm,+inf]
Default Value:| 0kNm


### Radius

Radius of wheel from center of axle to contact surface with rods.

   \          | physics:radius
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance
Default Units:| m
Range:        | ]0m,+inf[
Default Value:| 50cm


## TSTrack

Describes a track for a track joint to ride on. A track's 
geometry is defined by a curve, a twist and a general 
transforamtion. The latter is define by the xformOp operations.
The track specifies for it's ends to be connected with other track's ends.

   \          | TSTrack
------------- | ----------------------------
Inherits:     | Xformable
Parent Prim:  | TSTrackCollection, TSTrackSystem


### curve

Reference to a Bezier BasisCurves to define the geometry of the 
track.

   \          | curve
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | Relationship


### intervalNear

The location along the curve to start the track with.

   \          | intervalNear
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance
Default Units:| m
Range:        | ]-inf,+inf[
Default Value:| 0m


### intervalFar

The location along the curve to end the track with.

   \          | intervalFar
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | distance
Default Units:| m
Range:        | [-inf,+inf]
Default Value:| +inf


### frontConnection

Reference to a TSTrack that should be coupled with the 
front end of this track.

   \          | frontConnection
------------- | -------------------------
Type:         | Relationship


### frontConnectionEndType

End of referenced TSTrack to couple the front end of 
this track to.

   \          | frontConnectionEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### endConnection

Reference to a TSTrack that should be coupled with 
the end end of this track.

   \          | endConnection
------------- | -------------------------
Type:         | Relationship


### endConnectionEndType

End of referenced TSTrack to couple the end end of 
this track to.

   \          | endConnectionEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### trackBody

Reference to a physics and mass enabled body. This track will 
move with the body in the simulation.

   \          | trackBody
------------- | -------------------------
Type:         | Relationship


## TSConnectorCollection

A connector collection is a prim that contains connectors
(i.e. switches). It is used to group track connectors together.

   \          | TSConnectorCollection
------------- | ----------------------------
Inherits:     | Scope
Parent Prim:  | TSTrackSystem


## TSTrackCollection

A track collection is a prim that contains any 'TSTrack' 
prims. It is used to group tracks together.

   \          | TSTrackCollection
------------- | ----------------------------
Inherits:     | Xformable
Parent Prim:  | TSTrackSystem


## TSTrackSystem

A track system is a prim that contains any 'TSTrackCollection' 
prims. It is used to group track collections and switches together 
and to provide a reference for track joints to rail on.

   \          | TSTrackSystem
------------- | ----------------------------
Inherits:     | Scope


### metersPerUnit

The conversion factor from the units of the TrackCollections' 
and Tracks' Xform attributes to meters, when interpreted by 
the trax library. The trax system works with fixed units; 
this is no problem in a single USD file with its 'metersPerUnit' 
metadata properly set. However, if layers or references are 
used, the 'metersPerUnit' metadata in a given USD file is no 
longer respected. The lengthes of USD attributes get 
reinterpreted by the 'metersPerUnit' metadata of the stage. 
For religious reasons we don't believe in such a thing as a 
'scaled meter', hence we need to carry the proper scaling 
factor with us.

   \          | Meters Per Unit
------------- | -------------------------
Type:         | double
Dimension:    | distance
Range:        | ]0,+inf[
Default Value:| 1.0


## TS2WaySwitch

A two way switch reconnects three track ends according to 
the switches state.

   \          | TS2WaySwitch
------------- | ----------------------------
Inherits:     | Typed
Parent Prim:  | TSConnectorCollection


### divergingTrack

The track to connect with the incomming track at state 'branch'.

   \          | divergingTrack
------------- | -------------------------
Type:         | Relationship


### divergingTrackEndType

The end of the diverging track to connect.

   \          | divergingTrackEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### id

A unique id for sthe switch, to reference it. If 0, the switch
gets assigned an id automatically.

   \          | id
------------- | -------------------------
Type:         | int
Dimension:    | One
Range:        | [0,+inf[
Default Value:| 0


### narrowTrack

Reference to the incoming track of the switch.

   \          | narrowTrack
------------- | -------------------------
Type:         | Relationship


### narrowTrackEndType

End of the incoming track to connect.

   \          | narrowTrackEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]
Default Units:| 


 ### state
 
 The state of the switch.

   \          | state
------------- | -------------------------
Type:         | token
allowedTokens:| ["go", "branch"]


### straightTrack

The track to connect with the incomming track at state 'go'.

   \          | straightTrack
------------- | -------------------------
Type:         | Relationship


### straightTrackEndType

The end of the straight track to connect.

   \          | straightTrackEndType
------------- | -------------------------
Type:         | Dimensionated Value
allowedTokens:| ["front", "end"]


## TS3WaySwitch

A three way switch reconnects four track ends according to
the switches state.

   \          | TS3WaySwitch
------------- | ----------------------------
Inherits:     | Typed
Parent Prim:  | TSConnectorCollection


### divergingTrack1

The track to connect with the incomming track at state 'branch1'.

   \          | divergingTrack1
------------- | -------------------------
Type:         | Relationship


### divergingTrack1EndType

The end of the diverging track1 to connect.

   \          | divergingTrack1EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### divergingTrack2

The track to connect with the incomming track at state 'branch2'.

   \          | divergingTrack2
------------- | -------------------------
Type:         | Relationship


### divergingTrack2EndType

The end of the diverging track2 to connect.

   \          | divergingTrack2EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### id

A unique id for sthe switch, to reference it. If 0, the switch
gets assigned an id automatically.

   \          | id
------------- | -------------------------
Type:         | int
Dimension:    | One
Range:        | [0,+inf[
Default Value:| 0


### narrowTrack

Reference to the incoming track of the switch.

   \          | narrowTrack
------------- | -------------------------
Type:         | Relationship


### narrowTrackEndType

End of the incoming track to connect.

   \          | narrowTrackEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### state

The state of the switch.

   \          | state
------------- | -------------------------
Type:         | token
allowedTokens:| ["go", "branch", "branch1", "branch2"]


### straightTrack

The track to connect with the incomming track at state 'go'.

   \          | straightTrack
------------- | -------------------------
Type:         | Relationship


### straightTrackEndType

The end of the straight track to connect.

   \          | straightTrackEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


## TS1SlipSwitch

A single slip switch consisting of two incoming '','/' and
two outgoing tracks 'X' - the outgoing tracks are expected
to cross each other - and a diverging track ')'.
    
    \
    )X
    / 
    
   \          | TS1SlipSwitch
------------- | ----------------------------
Inherits:     | Typed
Parent Prim:  | TSConnectorCollection


### id

A unique id for sthe switch, to reference it. If 0, the switch
gets assigned an id automatically.

   \          | id
------------- | -------------------------
Type:         | int
Dimension:    | One
Range:        | [0,+inf[
Default Value:| 0


### incomingTrack1

Reference to first incoming track.

   \          | incomingTrack1
------------- | -------------------------
Type:         | Relationship


### incomingTrack1EndType

End of track referenced for first incoming track.

   \          | incomingTrack1EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### incomingTrack2

Reference to second incoming track.

   \          | incomingTrack2
------------- | -------------------------
Type:         | Relationship


### incomingTrack2EndType

End of track referenced for second incoming track.

   \          | incomingTrack2EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### outgoingTrack1

Reference to first outgoing track.

   \          | outgoingTrack1
------------- | -------------------------
Type:         | Relationship


### outgoingTrack1EndType

End of track referenced for first outgoing track.

   \          | outgoingTrack1EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### outgoingTrack2

Reference to second outgoing track.

   \          | outgoingTrack2
------------- | -------------------------
Type:         | Relationship


### outgoingTrack2EndType

End of track referenced for second outgoing track.

   \          | outgoingTrack2EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### state

The state of the switch.

   \          | state
------------- | -------------------------
Type:         | token
allowedTokens:| ["go", "branch"]


### track1Diverge

Reference to first diverging track.

   \          | track1Diverge
------------- | -------------------------
Type:         | Relationship


### track1DivergeIncomingEndType

End of track referenced for first diverging track.

   \          | track1DivergeIncomingEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


## TS2SlipSwitch

A double slip switch consisting of two straight tracks 'X', 
crossing each other; two incoming tracks, two outgoing tracks - all 
four connecting to the straight track ends - and two diverging 
tracks ')' and '(', connecting incoming and outgoing tracks:
    
    \ /
    )X(
    / \

   \          | TS2SlipSwitch
------------- | ----------------------------
Inherits:     | Typed
Parent Prim:  | TSConnectorCollection


### id
   \          | id
------------- | -------------------------
Type:         | Dimensionated Value
Dimension:    | One
Range:        | [0,+inf[
Default Value:| 0
 

 ### incomingTrack1

 Reference to first incoming track.

   \          | incomingTrack1
------------- | -------------------------
Type:         | Relationship


### incomingTrack1EndType

End of track referenced for first incoming track.

   \          | incomingTrack1EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### incomingTrack2

Reference to second incoming track.

   \          | incomingTrack2
------------- | -------------------------
Type:         | Relationship


### incomingTrack2EndType

End of track referenced for second incoming track.

   \          | incomingTrack2EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### outgoingTrack1

Reference to first outgoing track.

   \          | outgoingTrack1
------------- | -------------------------
Type:         | Relationship


### outgoingTrack1EndType

End of track referenced for first outgoing track.

   \          | outgoingTrack1EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### outgoingTrack2

Reference to second outgoing track.

   \          | outgoingTrack2
------------- | -------------------------
Type:         | Relationship


### outgoingTrack2EndType

End of track referenced for second outgoing track.

   \          | outgoingTrack2EndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### state

The state of the switch.

   \          | state
------------- | -------------------------
Type:         | token
allowedTokens:| ["go", "branch", "branch1", "branch2"]


### track1Diverge

Reference to first diverging track.

   \          | track1Diverge
------------- | -------------------------
Type:         | Relationship


### track1DivergeIncomingEndType

End of track referenced for first diverging track.

   \          | track1DivergeIncomingEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### track1Straight

Reference to first straight track.

   \          | track1Straight
------------- | -------------------------
Type:         | Relationship


### track1StraightIncomingEndType

End of track referenced for first straight track.

   \          | track1StraightIncomingEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### track2Diverge

Reference to second diverging track.

   \          | track2Diverge
------------- | -------------------------
Type:         | Relationship


### track2DivergeIncomingEndType

End of track referenced for second diverging track.

   \          | track2DivergeIncomingEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]


### track2Straight

Reference to second straight track.

   \          | track2Straight
------------- | -------------------------
Type:         | Relationship


### track2StraightIncomingEndType

End of track referenced for second straight track.

   \          | track2StraightIncomingEndType
------------- | -------------------------
Type:         | token
allowedTokens:| ["front", "end"]
