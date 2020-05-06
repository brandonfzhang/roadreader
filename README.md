## how to open the colab notebook

-[download this extension "open in colab"](https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo?hl=en)

-then go to [https://colab.research.google.com/github/](https://colab.research.google.com/github/)

-check the box "include private repos", it should take you to a github authorization screen

-authorize, then exit the page

-click the notebook you want to open (it should have a .ipynb file type)

-click the "open in colab" extension icon at the top right corner of the screen and it should open

## how to commit using colab

-select "save a copy in github"

-select this repo in the dropdown menu and select the appropriate branch

-unless you want to make a copy, keep the file name the same

-replace "Created using Colaboratory" with an actual commit message thanks

-no need to select "link to colab", then hit ok

## setting up raspi (add steps if you think anything is missing)

-[download this raspberry pi image file to your pc](https://drive.google.com/file/d/1JJifkjcFL7jgqRt8WhAlYyWapGxR-p-N/view)

-use win32 disk imager to write the file to the sd card

-run these commands in the following order to remove VNC credentials:

sudo systemctl stop vncserver-x11-serviced

sudo rm -rf /root/.vnc

sudo systemctl start vncserver-x11-serviced

~~-[install the sunfounder picar module](https://www.sunfounder.com/learn/SunFounder-PiCar-S/software-installation-picar-s.html)~~

~~-install tensorflow 1.14 (pip3 install tensorflow==1.14)~~

~~-install libhdf5 (sudo apt-get install libhdf5-serial-dev)~~

## Adding to the data set

- In dataCollectionOnlyCamera.py , set  filename to be the correct directory. You should change this between sessions so that if you screw up data collection, the bad data doesn't spoil all the previous data collected.

- Run dataCollectionOnlyCamera.py

- Holding down the '0' key saves pictures to the '0' subfolder. These photos should have no sign in them.

- Holding down the '1' key saves pics to its subfolder. These photes should have a stop-sign in them.

- Adding a yield sign later would use the '2' key and a '2' subfolder and more signs can be added similarly
