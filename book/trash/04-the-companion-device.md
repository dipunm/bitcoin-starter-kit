# Exploring the companion device
The companion device is a product called the Badger2040 created by a company called Pimironi. Pimironi is a hardware manufacturer that focuses on creating low cost tools and gadgets, mostly for educational purposes and conveniently accessible to the general public.

It has a total of 7 buttons: 2 on the back, and 5 on the front. It also has an LED on the bottom left, and an e-ink display (similar to the displays found on Amazon Kindles). The device requires no assembly, it is an all-in-one-piece device.

On the back, there are two buttons:
* a reset button marked as 'rst' on the top right corner,
* and a boot button marked as 'boot/usr'.

![buttons on the back of the Badger2040 device](./assets/2-buttons-back.png)

The reset button will reset the device when pressed, but the boot button is only useful for flashing firmware during setup. Although this button can be used by the application running on the device, the companion device's software does not make use of it due to its proximity to the reset button and how unintuitive it is to use.

On the front, there are three buttons along the bottom, and two on the side. The e-ink display will show the function of each key by displaying text just above each. If there is no label above a button, then the button has no use at that time.

![buttons on the front of the Badger2040 device labelled on the display](./assets/buttons-front.png){#fig:deviceFront}

Due to the lack of space, the user interface may be a little difficult to read. This book will act as a user manual to help you navigate the device as you learn how to use the device.

## Considering security vulnerabilities
The companion device is a simple computing device with only a small number of exploitable components. We will explore them in detail below.

As we explore this potentially scary, yet important topic, keep in mind how this section explores _potential_ vulnerabilities, and also describes the steps we have taken, and the steps you can take to minimise the chances of being exposed to exploits despite them. 

### The USB interface
While connected to a computer, the device is free to send and receive data including sensitive information on the device. Data could be leaked to the computer, or malware on the computer could be injected into the device.

Because the USB port requires a physical connection, we can clearly see what is connected to the device. While being used, it should not be connected to a computer; it should instead be connected to a power source such as a wall charger or a power bank.

Unfortunately many power banks will cut off power after a few seconds to the companion device because it draws such little power; from the commercial mobile devices that these banks are designed for, a low power draw would indicate that it is fully charged. The most safe and reliable source of power is a wall charger.

### Other physical connectors
The Badger2040 has other physical connectors on the back also. 

* It has a small 4 pin connector labelled 'qw/st' next to the reset button,
* and it has a series of exposed pins on the left side.

These connectors should have nothing attached to them, and just like the USB connector, check if they are connected to something and disconnect unless you are confident that it is not a security risk.

Note, that there is also a white battery connector on the back, this is purely a power connector and no risk to the security of your bitcoin.

A big benefit to the Badger2040 is its lack of wifi, bluetooth and other wireless communication modules. These modules would grant the device the ability to communicate with other devices and expose sensitive information without your knowledge.

### The persistent storage
The device has a 2MB of storage drive and 264kB of RAM (memory). Data stored in memory is temporary and is erased when the device loses power, but data on the 2MB of storage is kept even when the device is turned off; it will persist until deleted.

Malicious code running on the device has the ability to save sensitive or private information onto the storage; a private key is only 32 bytes long and can easily be stored on the disk many multiple times over.

Having sensitive data stored is not in itself very dangerous, however if the device is physically stolen or connected to a computer via USB, this sensitive data can be extracted and your bitcoin security would be compromised, potentially even without your knowledge of it.

The companion device will not attempt to store any sensitive data on the 2MB storage, but to ensure this, care should be taken (as described later in this guide) to ensure that the software installed is not malicious, and care should be taken to ensure that the device is never connected to an infected computer after use.

### The display
On the front, an e-ink display helps you to interact with the device by indicating what each button does on the bottom and right edges, and by displaying the results of your actions on the rest of the screen (see [@fig:deviceFront]).

The work we are doing on the device involves sensitive information, and that information will be presented on the display. It is therefore recommended that you ensure that there are no cameras or recording devices around that might capture the display of the device.

Being an e-ink display, it has a natural ghosting effect: content that was previously drawn may be faintly visible as you transition between pages. After showing sensitive information, the software may take a few seconds to "flash" the display; this is where the screen is cleared, turned black, and then cleared again. Flashing the device is an effective way to clear any sensitive information before continuing onto less sensitive operations, however it may take a few seconds to complete. 

Finally, when turned off, the display preserves whatever was last shown and cannot clear until powered on. This means that turning off the device while it is showing sensitive information is not recommended; however restarting or repowering the device will rectify the problem by starting a flashing operation and clearing the screen. After the screen is clear, it is safe to remove power from the device.

### The software
The companion device runs custom software which will detect button presses, interpret them, and update the display as it sees fit. This software has control of all components on the device, and can communicate with anything connected to it.

Being a general purpose device, the specific software that we will use is not pre-installed; this means that part of the setup will include finding and installing the software onto the device.

Later in this guide, we will walk you through some steps to take to ensure that the software that you install is an official, untampered, and uncompromised version. Without taking the appropriate precautions, it is possible to accidentally install malicious software designed to present incorrect or misleading information -- leading to you unknowingly protecting your money with an already compromised key.

Another potential vulnerability to consider is whether the software has any bugs or issues. One of the benefits of having the software publicly available online is that many security experts who are interested in the project can audit the project and report their findings on a public forum. The software is being scrutinized, not just by select professionals who have been paid to "certify" a product, but by many individuals who can also provide feedback publicly.

### The firmware
The firmware is code designed specifically for the microchips on the device. It is usually provided by the manufacturer of the device, and it sits between the software and the hardware.

For the most paranoid of users, the firmware is the last checking point for malware. Living between the software and the physical hardware, it has the ability to intentionally misinterpret the software to a limited extent. This can cause the device to show incorrect information, or to misinterpret your actions and ultimately, cause the software to behave differently to how you expected. If the different behaviour is subtle enough, you could once again be mislead.

This guide will walk you through downloading and installing the latest version of the official firmware before installing the software.