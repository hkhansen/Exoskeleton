# Upper adaptable upper-limp exoskeleton
In this repository, the files for creating a user-specific upper-limp exoskeleton can be found. The project was conducted as a master thesis project at the Department of Technology, Management and Economics at the Technical University of Denmark. The department is a part of the European [ReHyb](https://rehyb.eu/) project.
## Structure
- The *Configurator* folder contains all files used for the configurator, including a compressed file containing the executable program.
- The *SolidWorks files* folder contains the 3D models of all iterations of the exoskeleton.
- The *Control software* is in its own [repository](https://github.com/hkhansen/exoskeleton_control), as GitHub will not show repository folders within exoisiting repositories.


## Bill of components for Exoskeleton Mk3
To create the exoskeleotn, the following parts are needed.
### Manufacturing
- Normal size 3D printer (along the size of a Prusa i3 MK3S+)
- PLA filament
### Mechanical parts
- 22 M4x12 bolts
- 22 M4 nuts
- 1 M4 grub screw
- 1 M4 square nut
- 3 M3x12 bolts
- 4 M3x18 bolts
- 1 M3x6 bolt
- 3 M3 heated inserts
- 4 M3 6mm standoffs
### Electronics
- Raspberry Pi 3B or 4B
- [Adafruit DC & Stepper Motor HAT for Raspberry Pi](https://www.adafruit.com/product/2348)
- [AS5600 magnetic encoder](https://www.amazon.com/Magnetic-Encoder-Induction-Measurement-Precision/dp/B094F8H591?th=1)
- [ACS712 Current Sensor Module](https://www.amazon.com/NOYITO-ACS712-Current-Sensor-Detector/dp/B07D1W7GJJ/ref=sxin_15_ac_d_bv?ac_md=0-0-QnVkZ2V0IFBpY2s%3D-ac_d_bv_bv_bv&content-id=amzn1.sym.8f2bf95d-b9c2-4e6d-96a9-5fdf77a1951d%3Aamzn1.sym.8f2bf95d-b9c2-4e6d-96a9-5fdf77a1951d&crid=MZVO4L01JDNQ&cv_ct_cx=ACS712&keywords=ACS712&pd_rd_i=B07D1W7GJJ&pd_rd_r=7b714947-ff71-45f9-a34f-4d3698aa58d0&pd_rd_w=HtPKe&pd_rd_wg=SF9qO&pf_rd_p=8f2bf95d-b9c2-4e6d-96a9-5fdf77a1951d&pf_rd_r=0ZTBXDSWPY3ZQH3MBZ8D&qid=1675072088&sprefix=acs712%2Caps%2C144&sr=1-1-270ce31b-afa8-499f-878b-3bb461a9a5a6&th=1)
- [Adafruit ADS1115 16-Bit ADC](https://www.adafruit.com/product/1085)
- [DC Power Jack Female Panel Mounting Connector Socket](https://www.amazon.com/URBEST-x5-5mm-Female-Mounting-Connector/dp/B01M1D5GIP/ref=sr_1_10?keywords=dc+power+jack&qid=1675072249&sr=8-10) (optional)
## How to use (Not completed!)
This is a small guide on how to run the configurator program and how to set up the Raspberry Pi.
### Configurator
- Download the compressed file fitting your operating system.
- The file needs to be unzipped using either [WinRar](https://www.win-rar.com/start.html?&L=0) or [7-zip](https://www.7-zip.org/). Unzip it to a known location, like the desktop.
- Run the configurator by starting *Exoskeleton configurtor*.
- The generated STL files will appear in the folder containing the program.
- All static parts can be found in the *Static parts* folder.
### Preparing the Raspberry Pi
- Use the [Raspberry Pi imager](https://www.raspberrypi.com/software/) software for preparing a SD card.
- For the OS, choose Raspberry Pi OS or OS Lite.
- Choose the SD card as storage.
- Press Ctrl + Shift + X to enter the Advanced options.
- Enable SSH and set username and password. The default username is *pi*.
  - The hostname can also be changed. However, remember it for later.
  - The default hostname is *raspberrypi*.
- Configure wireless LAN with your network SSID and password.
- Press *Save* and then *Write*.
### Setting up the Raspberry Pi
- Power up the Raspberry Pi.
- SSH into the Pi from a PC on the same network.
  - For Windows users a terminal program like [PuTTY](https://www.putty.org/) is useful.
  - When starting up PuTTY, write *username@hostname.local* in the Host Name input field.
  - With a default Raspberry Pi the default hostname is: *pi@raspberrypi.local*
- Install git on the Pi with the commands (or move them unto the Pi with a USB drive. Comes in a later update):
```sh
sudo apt-get update
sudo apt-get install git
```
- Clone the control software files from the independt repository:
```sh
git clone https://github.com/hkhansen/exoskeleton_control.git
```
- Move to the control software directory, make the setup shell-script executable and run the script:
```sh
cd exoskeleton_control
chmod 755 setup.sh
./setup.sh
```
- When the setup is finished, the exoskeleton is ready to use. 
