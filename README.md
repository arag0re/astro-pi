# astro-pi demo

this is a demo written in python for the astro-pi project

## Setup AstroPi-Kit
### Get KitOS onto SD-Card
  Download AstroPi-KitOS from [here](https://downloads.raspberrypi.org/AstroPi_latest) and flash it using [RaspberryPi-Imager](https://github.com/raspberrypi/rpi-imager/releases) with no extra options enabled.

### Setup Hardware
  Then follow the [guide](https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/1) on how to assemble the Kit.

### Initial Boot
  After you essambled the Kit you can plug in the SD-Card and boot. But you cannot install and boot the device headless on the initial boot cause you need the accept the EULA. See [here](https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/2).

  So you will need to plugin peripherals aswell as a monitor with the cable that comes with the kit.
  After you accepted the EULA you can now follow the promts on the Screen to setup a user, language-settings and netwoking.
  
  🔴IMPORT HERE IS TO NOT UPDATE THE DEVICE!!!🔴 SO IN THE PROMPT ON INITIAL SETUP SKIP THE UPDATE PART!!!🔴

### Setup SSH and VNC
  Then you need to enable some settings to work smothly with the device. Go in a Terminal and type `sudo raspi-config` 
  or do it in the gui. search for `interfacing options` and enbale ssh aswell as vnc but you only really need ssh for development.
  for vnc to work you will need to do some more steps: 
    * Go in the terminal and execute the following commands: 
    *  
      ```
      vncpasswd -service //to change the default password!
      ```
   * then:
      ```
      sudo raspi-config nonint do_vnc 0
      sudo systemctl enable novnc
      sudo systemctl start novnc
      sudo systemctl unmask avahi-daemon
      sudo systemctl enable avahi-daemon
      sudo systemctl start avahi-daemon
      ```
  After those steps you will be able to access the astro-pi via:
  `https://astro-pi-kit.local/vnc.html` in your Browser (if you changed hostname replace url with the chosen hostname) 

### Setup IDE
* Download VSCode from [Microsofts Website](https://code.visualstudio.com/download)
    * Install [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) VSCode extension.
    * Press `F1` on your keyboard and search for `Remote-SSH: Add New SSH Host` and hit enter.
    * Enter `ssh username@raspiberrypi.local` (configured previously in raspberrypi imager) and hit enter on your keyboard. 
    * Then select the ssh-config file where you want to save this config to.
    * Press `F1` again and search for `Remote-SSH: Connect to Host` and hit enter.
    * Select the configured host `raspberrypi.local`.
    * Select `Linux` from the list as remote-host platform.
    * Enter the password for your user (configured previously in raspberrypi imager).
    * Now your VSCode is connected to your rapsi via SSH. You can use the integrated terminal (ctrl+shift+ö) to interact with raspberry pi's shell and install software via apt.
    
If you want to use SSH-Key instead of password you can do this with the following steps:
  * Download and install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
  * Generate a new rsa-key with puttygen and save the `.ppk` and save the OpenSSH Version of the Key aswell.
  * Copy and Paste the PUB-Key from the window in putty gen in an empty txt file to save it!
  * Connect to the AstroPi via SSH and create a Folder in you home folder called `.ssh` and then nano into `~/.ssh/authorized_keys` and paste your pubkey in there. save and exit with `ctrl+x` and then confirm with `y`.
  * edit your ssh-config to include the Key:
     ```
     IdentityFile C:\Path\to\pub\key\file
     ```
  
## how to run
  For this simple demo on an astro-pi-kit you wont need to install something additionally!
  if you want to run this on any other pi you will need python 3.9. 
  when you got the right python version installed you can just
  ```
  pip install -r ./requirements.txt
  ```
  to intall the needed packages.

  then execute the python script via:
  ``` 
  python3 ./index.py
  ```
