# Changelog  railOmniverse Extension (omni.rail.core)

## [Unreleased]

## [0.1.0] - 2022-10-28

### Added
- Project setup.
- PhysX custom track joint
- Simple feeder
- Feeder with motor model
- Dimensionated Values
- Tram.usda sample
- Locomotive.usda sample
- LocomotiveHit.usda sample
- EightVerySmall.anl4 auto loaded track system 

## [0.2.0] - 2022-11-21

### Added
- Simple rendering of trax tracks (for debug purposes).
- Reading 'BasisCurves' from USD.
- Track system creation from USD definitions.
- Tracks.usda sample with USD defined tracks.
- TestTrackSystem.anl4

### Changed
- Scaled samples to more realistic lengthes.
- Changed the locomotive in the samples from 'revolute joint' hinges to 'limited spherical joint' hinges.
- TrackSystem autoload to rel attribute in the trackjoint prim (temporarily)

### Fixed
- Fix for trackjoint interferrence after running over track end.

## [0.3.0] - 2022-12-16

### Added
- Switches: Two-way, three-way, single- and double slip switches.

### Changed
- Spherical joints for Locomotive samples. 
- Updated to Kit SDK 104.0.

## [0.4.0] - 2023-02-06

### Added
- Blue lines marking the trax tracks can be toggled on and off by left Alt key.
- Scaling of linear dimensions by arbitrary UsdGeomTokensType::metersPerUnit settings.
- Scaling of mass dimensions by arbitrary UsdPhysicsTokensType::kilogramsPerUnit settings.
- Multiple track systems.
- Tracks_modified.usda sample with scalings.

### Changed
- To be railed a track joint now needs a reference to a track system.

### Fixed
- Bug with rotational transformation using quarternions.

## [0.5.0] - 2023-02-15

### Added
- Tracks that reference a physical body are considered to be movable tracks, moving with that body.
- Tracks_movable.usda sample with movable track on rotatable beam.

### Changed
- Improved log messages.

### Fixed
- Crashes on invalid references in USD.
- Removed wrong dimensions in logging messages on derailing.

## [0.6.0] - 2023-03-02

### Changed
- Blue lines showing the track path disabled by default. (Enable by Left-Alt-Key.)

## [0.7.0] - 2023-03-03

## [0.8.0] - 2023-03-20

### Added
- PiecewiseDirectionalTwist; support for normals with BasisCurves.
- More uniform and detailed console log messages.
- Translation and rotation for TSTrack parent prim's transformation (Tracksystem prim).
- General transformations for curves.

### Changed
- Using stage's up direction for directional twist.
- If for a TSTrack no "curve" reference is given, but a BasisCurves is inside the prim, it is used as a curve for the track.
- Maximum Segment length for blue lines track painting (debug feature) lowered to 50m. Curve features smaller than that might still be missed.

### Fixed
- Double slip switch: branching tracks ends were wrongly connected.
- Problems with tangents on degenerated Bezier curves.

## [0.9.0] - 2023-03-30

### Added
- Scope prims can be used to group tracks and switches inside a track system.

### Changed
- Tracks.usda uses a Scope prim now to group the two switches.

## [0.10.0] - 2023-05-08

### Added
- Linux support.

## [0.11.0] - 2023-10-09

### Changed
- Updated to Kit SDK 105.1.

## [0.12.0] - 2024-05-14

### Added
- Create menu items for all railOmniverse prims.
- Import of *.anl4 files.
- Mesh generation for tracks.
- Introduced TrackSystem, TrackCollection, ConnectorCollection prim types.
- Tutorials.
- Demo Version.

### Changed
- Updated to new trax version 2.0.0.

### Fixed
- Changes to the TSTrack transformations get applied now.