# Exploring the companion device
## Exploring security vulnerabilities
The companion device is a product called the Badger2040 created by a company called Pimironi, a hardware manufacturer that focuses on creating low cost educational tools and gadgets. The Badger2040 is a simplified computing device with a relatively small number of exploitable components. We will explore them in detail below.

This section may go into details that are   

### The operating system
The device does not run a generic operating system like Microsoft Windows, Apple Macintosh or Linux, this means that it is unlikely to be targeted by hackers who are looking to infect as many devices as possible. This helps to reduce the threat level from opportunistic hackers to those who wish to target this product, or yourself directly. 

The operating system is really basic, unlike most generic operating systems that can do multiple things at a time, that are dealing with mice, printers, speakers, presenting its own windowing graphical interface, and many other things in the background that we don’t always appreciate, this device will only run the software that we put onto it and nothing else.

An attacker on a more complicated operating system would have many options for exploitation. Ignoring the communication devices like wifi, ethernet, and bluetooth, If a hacker were to compromise a computer or your external devices before you get it, or if they convinced you to infect your own computer by inserting untrusted USB devices, the range of ways they could exploit your computer would include:

- Pre-programming a USB mouse or keyboard to send malicious commands that instructs your operating system to misbehave.
- Installing viruses that run in the background, monitor your activity and record it for later capture.
- Exploiting known bugs to bypass security policies that the operating system relies on to keep you safe while providing its advanced feature set.
- Displaying fake warnings, errors, or notices that prompt you to take actions that are ill advised, such as revealing secret passwords to an untrusted application.

The more advanced an electronic device is, the more devices it has, the more multi-purpose it can be, the more apps it can install - all contribute to how vulnerable it is to such exploits.

Fortunately, the companion device is self contained, with only very simple buttons and a display. It has no wifi or bluetooth, however it does have a USB port which we will dive into more later.

### The USB interface
Because the USB port is not wireless, it is very obvious what is plugged into your companion device. Ideally, while being used, it should not be connected to another computer, it should instead be connected to a power source such as a wall charger or a power bank.

Unfortunately many power banks will cut off power after a few seconds to the companion device because it draws such little power; for mobile devices, a low power draw indicates that the mobile device is fully charged. Therefore, the most reliable source of power is a wall charger.

While connected to a computer, the device is open to sending and receiving data which means any sensitive information on the device may be extracted, and any malware on the computer may be injected into the device.

### The persistent storage
The device has a 2MB of storage drive and 264kB of RAM (memory). Data stored in memory is temporary and is lost when the device loses power, but data on the 2MB of storage is kept until deleted.

Malicious code running on the device has the ability to save sensitive or private information onto the drive, a private key is only 32 bytes long and can easily be stored on the disk many multiple times over. This in itself is not very dangerous, however if the device is stolen, that data can be physically extracted, and if the device is connected to another device via a complex protocol such as USB, then the data can be leaked too.

### The firmware
The firmware is effectively the operating system for the device. It is a good idea to install the firmware from a trusted source as an untrusted firmware could contain malicious code having similar risks as untrusted software.

### The software
The software itself could be malicious, or could have bugs that make it easy to compromise. To combat this, we keep the code free and open source. This allows interested security experts to audit it and will increase the chances that the code is trustworthy.

On a platform like https://github.com, there are tools that can be used to communicate risks and concerns. You can visit the website and look out for a few indicators to verify that the code is not vulnerable.

- In the “About” section on the right, you can see a watch count and a star count. These are indicators that let us know how many people are interested in the project and keeping an eye on it. Keep in mind however, it is not an indicator of how many of these people are security experts.
- Near the top, you may see an issues tab with a number next to it. This indicates that people have found bugs or are requesting new features. By clicking on the tab, you can see which it is. If there are many bugs, the code may be old and untrustworthy.

Other things you can do, is to do an online search for the name of the product with words such as “malicious”, “buggy”, or “dangerous” in order to see if there are articles or reviews by people who are reporting the software as such.

Malicious or buggy software has the ability to utilise the storage, usb connector, or even the display to either leak information, or to mislead the user. A computer that lies to you can be critical when dealing with security focused or sensitive work.
