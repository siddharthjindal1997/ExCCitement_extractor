# ExCCitement_extractor

## Python based sports video highlights extraction tool 

## Note

ExCCitement_extractor is a GSoC 2017 project under [**CCExtractor organisation**](http://ccextractor.org/).

Mentor - [Zulko](https://github.com/Zulko)

Project link - [GSoC](https://summerofcode.withgoogle.com/projects/#5422945299070976)

Blog Posts - [GSoC blog](http://www.medium.com/@siddharthjindal1997)

## First release : v0.1

Excitement_extractor is a Python based software which uses the concept of excitement modelling to automatically extract highlights of a Sports match.

It models a video input into a Excitement vs time curve, which is then be used for to extract automatic highlights. The graph shows the change in the excitement trend of the video with peaks-and-lows marking interesting-and-boring moments af the match and then uses this graph to generate automatic highlights. 

## Current Status 

The project proposal is completed. The first version (v0.1) of the software is ready to be used. 
The software works quite well for soccer matches. It takes around 15min extraction time for a 90 min long match. It has been tested on several soccer matches and works quite well. 

Apart from just goals, the software is able to include in highlights some very crucial moments of a match like big fouls, close attempt towards goal or any event which might be exciting to watch for audience.

Other than soccer the software works well on other sports like Rugby/Hockey to atleast generate the Excitement trend of the game. Games like cricket, tennis, basketball tend to be a bit monotonous for this software. Thus it does not provide very good insights of these and similar sports.

The software has its own GUI built in Qt. Thus it's a cross platform software without requirement of command line. 
The GUI is still in its early phases. It allows user to load a file, generate graph and extract highlights to an MP4 video.


#### Dependencies:

* [Python 2.7.X](https://www.python.org/downloads/)

* [MoviePy](https://github.com/Zulko/moviepy) - To read, write and process video file.

* [Numpy](https://www.numpy.org/) - to handle mathematical operations.

* [Matplotlib](https://matplotlib.org/) - to generate graph and plots.

## Download & Installation

1. Clone the repository.
	`git clone https://github.com/siddharthjindal1997/ExCCitement_extractor.git`
	Or you can download the zip file and Extract the files from there.

2. Download dependencies (see below)

3. change directory (cd) to `/ExCCitement_extractor/ExCCitement_extractor` folder and run `python main_gui.py` from terminal.
	(make sure you are using python version 2.7.x )

## Installing dependencies

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

### Manual installation

	1. python version 2.7 install (if does not exsist)
	`sudo add-apt-repository ppa:fkrull/deadsnakes`
	`sudo apt-get update`
	`sudo apt-get install python2.7`

	2. Download moviepy through pip.
	`sudo pip install moviepy `

	3. Download matplotlib
	`sudo apt-get install python-matplotlib`

	4. download pyqt4
	`sudo apt-get install python-qt4 `


## Usage 

The usage of the software is quite simple. Firstly run the GUI.
To load a new file click on `load file` button. Or you can select `load` from the menu bar.
Click `Generate excitement graph and Extract highlights` button to start the process of extraction.
Check the Text box in the lower region for log outputs.
click cancel to stop a processing file.
Click `Exit` to quit the software.

## Known issues 

* Progress bar is currently visible in the terminal. This needs to be included in the GUI.

## To-Do (Immediate work)

* Solve known issues.

* PyPi package upload.

* Improve the GUI and convert it into a Sports-match assistent Video player.

## Future plans
* Compare two different matches to know which one is more exciting.

* The current algorithm will be extended for exitement modelling of various categories of videos (like movies, sitcoms etc.) which will lead to the main aim of extraction of interesting bits from any kind of video.

## Licences

I have not decided the licence for the project yet. All the individual licenses of libraries and code used can be found under `license/` directory.
Although I have tried to maintain the licenses for each library used in the project, any kind of error is possible. In such case please feel free to reach out, and accept my apologies. I’ll be happy to correct my mistakes.



## Contributing

The project is under constant development. It needs a good amount of enhancement and thus any contribution is welcome. 
For more info on contributing read [contributing.md](https://github.com/siddharthjindal1997/ExCCitement_extractor/blob/master/docs/contributing.md).