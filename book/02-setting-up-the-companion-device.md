TODO... Create installer and document the installer

https://www.raspberrypi.com/documentation/microcontrollers/rp2040.html  

# Setting up the companion device
In order to follow along in this section, you will need a desktop or laptop computer, and you will need to be computer literate. If you are finding this section difficult, feel free to ask a trusted friend or family member to help; we will not be dealing with any sensitive information in this section.

Setting up the Badger2040 takes 2 steps:

1. Installing the latest firmware.
2. Uploading the custom software.

**The firmware** is the manufacturer's software designed to work with the peripherals and hardware as it is configured on the device. Once installed, it typically does not need to be updated very often, however it is a good idea, upon receipt, to install the latest firmware to be sure that we have the most efficient, feature rich, bug free firmware available.

**The custom software** interacts with the firmware in order to communicate with the hardware, and it is responsible for coordinating the user experience, reacting to button presses, and plotting the images for the display to draw; amongst other things. The firmware is pretty dumb but necessary and the software is the brains of the operation.

## Installing the firmware
The latest information regarding this part of the setup is detailed as part of the offical getting started guide: 

> <https://learn.pimoroni.com/article/getting-started-with-pico>

We will focus on the relevant parts of the guide here, however some details are subject to change. If you would like to learn more about the device or are having issues following along, consider reading the official guide as well.

In order to install the firmware, we will be:

- Downloading a **flash** uf2 file.
- Downloading a **firmware** uf2 file.
- Connect the device into "bootloader" mode.
- Copy the flash u2f file onto the device.
- Connect the device into "bootloader" mode again.
- Copy the firmware u2f file onto the device.

### Preparation
Before we start, we will need to download a couple of files. The first is a factory reset file which can be found on the official RaspberryPi website at: 

> <https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#resetting-flash-memory>

In the "Resetting flash memory" section on the website referenced above, there should be a link to download a `UF2 file`, and it will dowload a file named similarly to: `flash_nuke.uf2`.

The next file we will need is the latest firmware. This file can be found at: 

> <https://github.com/pimoroni/pimoroni-pico/releases>

Releases will be marked as "Latest" or "Pre-release"; look for the first one marked "Latest" and click on the version number.

Near the bottom of the page, you should see a link to a file labelled similarly to: 

> `pimoroni-badger2040-...-micropython-without-badger-os.uf2`

This is the basic firmware required to operate the device and nothing more. Keep both files in a folder that you can easily find and access later on.

### Connecting the device
The next thing we need to do is to connect the device to the computer. The device can be connected using a USB-C data cable and once connected, you will need to take a few extra steps to update the firmware.

On the back of the device, you will see two buttons labelled `boot/usr` (boot), and `rst` (reset), respectively. While _holding down_ the boot button, press the reset button to start the device in "bootloader mode". Your computer will detect and notify you of a new external drive connected.

Open the new drive; It may be labelled `RPI-RP2`. You may see the following two files:

- INDEX.HTM
- INFO_UF2.TXT

Copy the `flash_nuke.uf2` file to sit alongside these files. After the file transfer has completed, the device will disconnect itself and restart.

Physically disconnect the device via the USB cable, reconnect, and once again hold the boot button and press the reset button. When you open the drive again, you will see that your `flash_nuke.uf2` file was deleted; this is absolutely normal.

Copy the `pimoroni-badger2040-...-micropython-without-badger-os.uf2` file to the drive. This file will be larger and may take a few seconds to copy, but after completion, the device will disconnect itself and restart again.

At this point, you have installed the latest firmware. Don't forget to clean up and delete the two `uf2` files from your computer; you don't need them anymore.

## Installing the software

In order to install the software, we will be:

- Downloading the software.
- Verifying the download.
- Installing **rshell**.
- Uploading the software onto the device.

