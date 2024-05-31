railOmniverse
========================


Introduction
------------

**railOmniverse is an extension** to the [NVIDIA Omniverse Environment](https://developer.nvidia.com/omniverse) \[[1](#[1])\]. railOmniverse makes available railroad simulation functionality from the Trend trax library to Windows and Linux platforms.

**The demo version of railOmniverse** is a free version of the extension. It is limited in functionality and is intended to give an impression of the capabilities of the full version. 

The general functionality, the trax library provides, is described in [this book](https://www.trendverlag.com/Trax/Doc/Book/index.html) \[[5](#[5])\]; an overview is given with the article ['Trax Track Library'](https://www.trendverlag.com/Trax/Doc/BlogArticle/traxLibrary.html) \[[3](#[3])\]

An overview about the actual development of the railOmniverse extension, you'll find on the main page of the [railOmniverse Manual](https://www.trendverlag.com/Trax/Doc/Book/chapter12.html) \[[6](#[6])\].
 

Manual
------

**The manual** of the railOmniverse extension you'll find online with the [railOmniverse Manual](https://www.trendverlag.com/Trax/Doc/railDocumentation/Html/index.html) \[[7](#[7])\].
 

Tutorials
---------

**The tutorials** for the railOmniverse extension you'll find in the 'Tutorials' section of the [railOmniverse Manual](https://www.trendverlag.com/Trax/Doc/railDocumentation/Html/index.html) \[[7](#[7])\].

**The videos** of the tutorials will apear in the [railOmniverse Youtube playlist](https://youtube.com/playlist?list=PLvSXZtqqeOvBoA_W5E5gI6Hz2sxWsNI45&si=MDgvXsvM8kbBZEPy) \[[8](#[8])\].


Support and Newsletter
----------------------

**On problems, ideas, suggestions and things you desire** contact us at: horstmann.marc@trendverlag.de. To sign up for the railOmniverse newsletter, include ‘railNewsletter’ in the subject line.


First Steps
-----------


### Step 1 - Install the railOmniverse Extension

(this step can be omitted if the extension can be discovered from the extension
window directly.)

Assuming you have a zipped package of the railOmniverse extension 
under your fingertips, you can install it by extracting it to a proper
folder. That we have to find or create first:

- Start 'Isaac Sim' or another Omniverse based application, you want to
work with.
- From Menu -> Window -> Extensions open the 'Extensions Window'.
- On the 'hamburger button' on top of the 'Extensions Window' select
'Settings'.

Here you'll see the 'Extensions Search Paths' from which you can select
a folder to install the extension. You also can create a custom folder.
For now we decide for 'c:/users/[user]/documents/kit/shared/exts' which
is available for several Omniverse applications.

- Unpack the railOmniverse.zip into the folder you just decided for.

Now you can find the railOmniverse extension in the 'Extensions' window.


### Step 2 - Enable the railOmniverse Extension

An installed extension has to be enabled before it can be used.

- In the 'Extensions Window' find the railOmniverse extension by typing
in 'rail' in the search field.
- Select the 'omni.usd.schema.rail.core' extension and activate 'AUTOLOAD' 
by clicking the checkbox.
- Do the same for the 'omni.rail.core' extension.
- Now restart the application and visit the 'Extensions Window' again.

It should look like this:

<a href="./Images/ActivatingExtensions.png">
<img src="./Images/ActivatingExtensions.png" title="Find and enable these 
extensions." alt="Enable omni.rail.core and omni.usd.schema.rail.core." 
width="500px">
</a>


### Step 3 - Load the Test Files

The railOmniverse extension comes with a set of test files in the data
folder of the extension. You can load them to get a first impression of
the functionality.

- In the 'Content Panel' find the path you installed the extension.
- In the omni.rail.core folder find the data folder.
- Load the 'TestTrain.usda' file by double clicking it.
- From the toolbar to the left hit 'Play' to start the simulation.

<a href="./Images/CoupledTrain.png">
<img src="./Images/CoupledTrain.png" title="Train" alt="A train starting to run." 
width="500px">
</a>

- Hit the left alt key to toggle the track system visualization. It shows 
two thin blue lines were the rods actually are, while a track model can be 
moved out of sync with it.
- Try to manipulate a model by shift-clicking it and moving the mouse.

There are more test files to load, most of which start with 'Test...', while the ones
that do not are referenced by them, so they lack lights if you open them.
Under te folder 'Test', you'll find more abstract tests that show special functionality.
Mind the Tests/Tracks_movable.usda file, which shows a track that can be moved,
while something railed on it reacts accordingly.


### Step 4 - Find the Sample Files for this Tutorial

The sample files for this tutorial can be found in the 'docs/Tutorial' folder
of the extension. The tutorial itself is best viewn from this web page:

https://www.trendverlag.com/Trax/Doc/railDocumentation/Html/index.html


References
----------

\[1\] [NVIDIA Omniverse](https://developer.nvidia.com/omniverse)  
\[2\] [Simulating Railroads with OpenUSD, Marc-Michael Horstmann](https://developer.nvidia.com/blog/simulating-railroads-with-openusd/)  
\[3\] [The Trax Track Library, Marc-Michael Horstmann](https://www.trendverlag.com/Trax/Doc/BlogArticle/traxLibrary.html)  
\[4\] [railOmniverse, Marc-Michael Horstmann](https://www.trendverlag.com/Trax/Doc/BlogArticle/railOmniverse.html)  
\[5\] [trax book](https://www.trendverlag.com/Trax/Doc/Book/index.html)  
\[6\] [Chapter 12](https://www.trendverlag.com/Trax/Doc/Book/chapter12.html)  
\[7\] [railOmniverse's Documentation](https://www.trendverlag.com/Trax/Doc/railDocumentation/Html/index.html)   
\[8\] [railOmniverse Playlist on YouTube](https://youtube.com/playlist?list=PLvSXZtqqeOvBoA_W5E5gI6Hz2sxWsNI45&si=MDgvXsvM8kbBZEPy)  
