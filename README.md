# ExCCitement_extractor

## Python based sports video highlights extraction tool 

## Note

ExCCitement_extractor is a GSoC 2017 project under [**CCExtractor organisation**](http://ccextractor.org/).
Mentor - [Zulko](https://github.com/Zulko),
Blog Posts - [GSoC blog](http://www.medium.com/@siddharthjindal)

### First release : v0.1

Excitement_extractor is a Python based software which uses the method called excitement modelling to automatically extract highlights of a Sports match.

It models a video input into a Excitement vs time curve, which is then be used for to extract automatic highlights. The graph shows the change in the excitement trend of the video with peaks-and-lows marking interesting-and-boring moments af the match and then uses this graph to generate automatic highlights. 


#### Dependencies:
* [Python 2.7.X]
* [MoviePy]
* [Numpy]
* [pandas]

## Download & Installation

### Using conda (recommended)

1. Download [miniconda](https://conda.io/miniconda.html) with the python version available in your system.

2. Create a new environment for python version2.7 (if does not exists) :  
` conda create --name myenv python=2.7 `

3. Activate the environment by :
` source activate myenv `

4. To download dependencies in the environment run the following commands:

	* MoviePy installation: automatically installs numpy, ffmpeg and some other dependencies.
	` conda install -c conda-forge moviepy `

	* Matplotlib and PyQt4 installation
	` conda install matplotlib `

	* PyQt4 installation
	` conda install -c menpo pyqt `



## Current Status 

The project proposal is completed. The first version (v0.1) of the software is ready to be used. 
The software works quite well for soccer matches. It takes around 15min extraction time for a 90 min long match. It has been tested on several soccer matches and works quite well. 

Apart from just goals, the software is able to include in highlights some very crucial moments of a match like any big foul, close attempt towards goal or any event which might be exciting to watch for audience.

Other than soccer the software might work well on other sports like Rugby/Hockey to atleast generate the Excitement trend of the game.

The software has its own GUI built in Qt. Thus it's a cross platform software without requirement of command line. 
The GUI is still in its early phases. It allows user to load a file, generate graph and extract highlights to an MP4 video.



## Known issues 

* Progress bar not shown

## To-Do (Immediate work)

* Solve known issues

* Improve the GUI and convert it into a Sports-match assistent Video player.

* 

## Future plans
* Compare two different matches to know which one is more exciting

* The current algorithm is expected to be extended for exitement modelling of various categories of videos (like movies, sitcoms etc.) which will lead to the main aim of extraction of interesting bits from any kind of video.

### Note

ExCCitement_extractor is a GSoC 2017 project under [**CCExtractor organisation**](http://ccextractor.org/).
Mentor - [Zulko](https://github.com/Zulko)


