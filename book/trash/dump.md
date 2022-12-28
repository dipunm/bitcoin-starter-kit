&nbsp;
\newpage






Now is a good time to explore our options and scrutinze each one so we can choose our own preferred method.

The options we'll explore are:

- Calculating by hand
- Using the companion device
- TailsOS
- Other secure devices
- Make it up

In each case, you should get back a checksum in the form of a hexadecimal character. Append this to your last code, and you can use the "mnemonic words lookup" book to identify the final word of your BIP-39 mnemonic phrase.

### Calculating by hand
Technically, it is possible to calculate the checksum by hand, however it is not easy, is very error prone and is long and tedious. If you want to try it, there are videos online that will show you how to do it.

Calculating by hand involves:

1. Translating your X's and O's into 1's and 0's respectively to produce a binary number.
2. Performing a SHA256 calculation on the full 128 digit binary number.
3. Taking the first character from the resulting hash.

The first character is your checksum in hexadecimal form.

### Using the companion device
1. Read the companion device security pages
2. Power your device using a wall socket
3. Choose the checksum option from the homepage
4. Enter your hexadecimal codes
5. The device will reveal your checksum as a hexadecimal character

### TailsOS
1. Read the tailsOS security pages
2. Create a bootable TailsOS USB drive
3. Boot into TailsOS
4. Configure "offline mode" in the additional settings section
5. Log in
6. Launch the text editor
7. Enter the following text:
```text
#!/bin/bash
INPUT=$(echo "$@" | tr -d ' ')
BASE2=$(echo "obase=2; ibase=16; $INPUT" | bc | tr -d '\\\n')
PADDED=$(printf "%140s" "$BASE2" | sed 's/ /0/g')
BINARY=$(echo $PADDED | fold -w 12 | cut -c2- | tr -d '\n')
ASCII=$(echo "obase=16; ibase=2; $BINARY" | bc | xxd -p -r)
HASH=$(echo $ASCII | openssl dgst -sha256 | awk '{print $2}')
echo ${HASH:0:1} | tr '[:lower:]' '[:upper:]'
```

```text
#!/bin/bash
ARGS=$(echo ${@^^} | tr -d " ")
n=${#ARGS}; [ $n -ne 35 ] \
  && echo "E:H35 $n"  &2 \
  && exit 1
HEX=$(echo "${ARGS}0" | fold -w 3)
OUTPUT=$(echo "obase=2;ibase=16; $HEX" | bc \
  | rev | cut -c-11 | rev \
  | xargs printf "%145s" "obase=16;ibase=2;" | bc)
HASH=$(echo "$OUTPUT" | xxd -p -r \
  | openssl dgst -sha256 | cut -d " " -f2)
echo ${HASH^^} | cut -c1
```
8. Save the file as checksum.sh in the home directory
9. Launch the Files application
10. Right click and select "Open in Terminal"
11. Type: `sha256sum checksum.sh` and press enter
12. You should see a hexadecimal code beginning and ending with: `12a55...a945a`
13. Type: `bash checksum.sh`, followed by your hexadecimal codes and then hit enter.
14. You should see your checksum printed in hexadecimal form as a single character.

### Make it up

Unfortunately, calculating a checksum by hand is a very long, very laborious task. We really need to use a computer for this step, or we need to cheat.


There are a few ways to create our checksum safely including:

1. Use a specialised "airgapped" computer
2. Calculate it by hand (very difficult, not recommended)
3. Use a clean laptop running TailsOS

#### Airgapped
An airgapped computer is one that has no wifi, bluetooth or radio that could be used to leak sensitive information. Our companion device is one such device, however others include:

- Old fashioned calculators (although not useful for our use case)
- Airgapped hardware wallets
- Computers with their communication chips desoldered and removed

Temporarily disabling or blocking wireless signals from a device is not enough if the device has a storage disk that it could use to save the sensitive information for later.

#### TailsOS
A laptop running TailsOS is an interesting solution. TailsOS is an opensource operating system that can be installed onto and run from a USB drive. The software is privacy focused, and is therefore vetted and constantly being scrutinised from a privacy and security perspective.

TailsOS is designed to run on your personal computer, independently from your typical operating system. This allows it to run without any of the hidden viruses and malware that you might have collected through typical personal use, including those that even anti-viruses cannot detect.

When using TailsOS, we hope that our computer or laptop has not been physically compromised; although viruses have been circumvented, things like keyloggers, compromised chipsets inside your computer and low level firmware infections can undermine the privacy and security efforts of TailsOS. The official website explains this in more detail in their "untrusted computers" section.



