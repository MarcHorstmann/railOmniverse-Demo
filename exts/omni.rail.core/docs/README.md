# railOmniverse Extension {#mainpage}

The railOmniverse extension is a set of tools to simulate railroad vehicles in the NVIDIA Omniverse environment. It is based on Trend's 'trax library'[3] that was created by Trend Verlag[4] since 2014 to support several railroad simulation titles, directed at consumers. With the railOmniverse extension Trend Verlag aims to make the functionality of the 'trax library' available to Omniverse in a step by step manner, guided by the actual needs of customers. So feel free to contact Trend with your requirements.


## Introduction

The core of the trax library is the so called 'track joint' that keeps an object aligned with a track. It is a set of constraints communicated to the physics engine directly, so it works seamless with other forces and constraints in the simulator. It is implemented as a NVIDIA PhysX custom joint directly.

From here on outwards other library elements have been built. Of course the first things are tracks and track systems, editing them and solving an abundance of geometrical problems. For the track joint to work, several kinds of 'feeders' exist that relay the track's geometry to the track joint and provide a motor model. Next the trax library offers support for wheel frames and bogies and the assemblies of such, called 'rolling stock'. From rolling stock train's are built. Then you need means for communication with those steaming trains; so the trax library provides a 'sensor system' and a 'signal system'. Then you want to build logic that is simple and stays that way; so the trax library provides a bulletproof 'Jacks & Plugs system'. And on and on it goes if it comes to cargos or passengers or switch boards or ...


## Content

Here comes a list of the content that is available in the railOmniverse extension so far:

### Functionality:

- Dimensionated values with units.
- Track joint with basic feeder.
- Track joint with a motor model feeder, featuring a 'traction force characteristic'; i.e. a WheelFrame object.
- Track system, including:
	+ Two way switches.
	+ Three way switches.
	+ Single slip switches.
	+ Double slip switches.
- Simple track editing, based on Omniverse cubic Bezier curves.
- USD import of *.anl4 - files, the native file format of the trax library. Here with 'Eisenbahn.exe Professional (EEP)' a full fleged track system editor is available.
- Mesh generation for tracks.

### Assets:

These assets are meant for testing and demonstration purposes only. They are not meant for production. If you are interested in railroading assets for production purposes, please contact Trend Verlag. Trend is happy to provide for your wants - under a license suited to your needs.

- EightVerySmall (A compact track system).
- TestTrackSystem (A slightly less compact track system).
- TwoWaySwitch (A single switch with a loop).			 
- TestTwoWaySwitch.usda (setup with TwoWaySwitch and TRAXX147)
- ThreeWaySwitch (A three way switch with two loops).
- TestThreeWaySwitch.usda (setup with ThreeWaySwitch and TRAXX147)
- DKW190.usda (A double slip switch with two loops).
- TestDKW.usda (setup with DKW190 and TRAXX147)
- EKW190.usda (A single slip switch with two loops).
- TestEKW.usda (setup with EKW190 and TRAXX147)
- TRAXX147.usda (A locomotive).
- LogWagon.usda (A wagon).
- Train.usda (A train consisting of the locomotive and six of the wagons).
- TestTrain.usda (setup with TestTrackSystem and Train)
- Tests/Tram.usda (A two section track vehicle with three bogies, the middle one being a jacobs bogie. Each carries a trackjoint to make it railable. One of the trackjoint's motors is preconfigured with a target velocity and force limits to make the vehicle run).
- Tests/Locomotive.usda (A 'locomotive' with two bogies. One carries a trackjoint. This makes up the simples configuration in which to use a trackjoint. The other bogie carries a PhysicsWheelFrame to use a motor model feeder. It contains the trackjoint as well as two wheelsets and a reference to a traction force charactersistic. To make the locomotive run, for the wheel frame set a fraction of the thrust and brake (e.g. 0.5) and specify a target velocity. Change the sign of the target velocity or put it to 0 and see what happens. On running too fast around the curve, the vehicle will derail).
- Tests/LocomotiveHit.usda (A ball hits our locomotive; locomotive starts to move, but due to friction will come to rest after running two times the loop. This shows that the trackjoint is a bunch of real physics constraints and not a kinematical method to just move things).
- Tests/Tracks.usda (A locomotive runs along a track system defined by USD in the same file).
- Tests/Tracks_modified.usda (A scaled locomotive on a single track. meters_per_unit set to 1).
- Tests/Tracks_movable.usda (A locomotive on a three tracks track system with the middle one being movable connected to a body).
- Tests/PiecewiseDirectionalTwist.usda (Several tracks, using the normal definition of BasisCurves for the twist calculation. General up direction of the file is "Y").

### Documentation:

- 5 Tutorials[1] for getting started .
- A reference[1], documenting the available prim types .
- The trax book Chapter 12[2]. A chapter of trax Book with a detailed information about the railOmniverse extension.
- The trax Book[3], a book about the trax library.

### Demo Version:

The demo version of the railOmniverse extension is available for free. It contains everything the full version has, but it is limited in the following ways:

- Maximum of 14 track joints.
- Only 1 switch.
- Maximum of 34 tracks.


## Future Development

The speed and the general order of future development depends largely on the feedback of the railOmniverse users; it includes but is not limited to:

- Create library of standard traction force characteristics.
- BasisCurves: implement support for more than cubic Bezier curves.
- RollingStocks
- Trains
- Track Models Generator
- Sensors
- Signals
- Jacks & Plugs
- ...

Please take a look at the 'trax book' Chapter12 for more detailed and more recent information. Write Trend an e-mail at horstmann.marc@trendverlag.de for feedback or if you look for a full version of railOmniverse. Trend is happy to provide for your wants - under a license suited to your needs.


## References

- [1] railDocumentation : https://www.trendverlag.com/Trax/railOmniverse/source/extensions/omni.rail.core/docs/Html/index.html
- [2] Chapter 12: https://www.trendverlag.com/Trax/Doc/Book/chapter12.html
- [3] Trax Book: https://www.trendverlag.com/Trax/Doc/Book/start.html
- [4] Trend Verlag: https://www.trendverlag.com
- [5] Trend Shop: https://www.eepshopping.com







