# Using your first key
Congratulations! You have created your first private key!

By now you have your first set of 12 words, but it's pretty useless by itself. In order to use the key, you're going to need some sort of wallet. Bitcoin wallets come in many shapes and sizes, from specialised hardware (often called signing devices or hardware wallets), to mobile applications running on your personal smart phone.

This is the moment that we decide the fate of our new key:

- Is it going to store a small amount of bitcoin?
- is it going to be used to secure our savings?
- or will it be completely offline and used only for receiving money until some time in the future? -- like a one time use piggy bank, but made from several inches thick steel.

Most of us will start by creating spending wallets and then progress to making saving wallets. We will experiment with many different types of spending wallets as we learn more about the ways we can use our bitcoin, but somewhere along the way, we will want to keep some bitcoin safely aside, somewhere that we can top up at any time and where its security is unaffected by our daily activities.

It is important to separate the concept of a **private key** and a **wallet**. The term wallet is pretty overloaded with respect to bitcoin, but in general a wallet is a piece of hardware or software that stores, manages, or uses your private keys (and in some cases, your public keys).

After obtaining a wallet, you may discover that it offers you the ability to create multiple wallets. This is because the term wallet also refers to the 


this symbol: `→`.
```bash
#!/bin/bash
ARGS=$(echo→${@^^}→|→tr→-d→"→")

n=${#ARGS};→[→$n→-ne→35→]→\
→→&&→echo→"E:H35→$n"→>&2→\
→→&&→exit→1

HEX=$(fold→-w→3→<<<→"${ARGS}0")

BIN=$(bc→<<<→"obase=2;ibase=16;$HEX"→\
→→|→xargs→printf→"%012d\n"→\
→→|→rev→|→cut→-c-11→|→rev)

OUTPUT=$(echo→"obase=16;ibase=2;"→\
→→$(printf→"%s"→$BIN)→|→bc)

HASH=$(echo→"${OUTPUT:0:32}"→|→xxd→-p→-r→\
→→|→openssl→dgst→-sha256→|→cut→-d→"→"→-f2)

echo→${HASH^^}→|→cut→-c1
```


```bash
#!/bin/bash
ARGS=$(echo ${@^^} | tr -d " ")

n=${#ARGS}; [ $n -ne 35 ] \
  && echo "E:LEN $n" >&2 \
  && exit 1

grep -qvE "^[0-9A-F]+$" <<< "$ARGS" \
  && echo "E:RANGE" >&2 \
  && exit 1

HEX=$(fold -w3 <<< "$ARGS"0)

BIN=$(bc <<< "obase=2;ibase=16;$HEX" \
  | xargs printf "%012d\n" \
  | rev | cut -c-11 | rev)

OUTPUT=$(echo "obase=16;ibase=2;" \
  $(printf "%s" $BIN) | bc)

SHA=$(echo "${OUTPUT:0:32}" | xxd -p -r \
  | openssl dgst -sha256 | cut -d " " -f2)

echo ${SHA^^} | cut -c1
```

```bash
#!/bin/bash

# Uppercase and remove spaces
ARGS=$(echo ${@^^} | tr -d " ")

# Validate length: 35 characters
n=${#ARGS}; [ $n -ne 35 ] \
  && echo "E:LEN $n" >&2 \
  && exit 1

# Validate character range: 0-F (hexadecimal)
grep -E "[^0-9A-F]" <<< "$ARGS" \
  && echo "E:RANGE" >&2 \
  && exit 1

# Append 0 for last character and split into 12 chunks
HEX=$(fold -w3 <<< "$ARGS"0)

# Convert to base2 (binary),
# format as 12 bit with leading 0s,
# and drop first bit from each chunk
# This gives us the original random number in base2
BIN=$(bc <<< "obase=2;ibase=16;$HEX" \
  | xargs printf "%012d\n" \
  | rev | cut -c-11 | rev)

# Convert to base 16 (hexadecimal)
OUTPUT=$(echo "obase=16;ibase=2;" \
  $(printf "%s" $BIN) | bc)

# Take first 16 bytes (128 bits)
SHA=$(echo "${OUTPUT:0:32}F" | xxd -p -r \
  | openssl dgst -sha256 | cut -d " " -f2)

# Uppercase and print first character
echo ${SHA^^} | cut -c1
```

```
#!/bin/bash
A=$(echo ${@^^}|tr -d " ")
H=$(fold -w3<<<"$A"0)
B=$(bc<<<"obase=2;ibase=16;$H"|xargs printf "%012d\n"|rev|cut -c-11|rev)
O=$(echo "obase=16;ibase=2;"$(printf "%s" $B)|bc)
S=$(echo "${O:0:32}"|xxd -p -r|openssl dgst -sha256|cut -d " " -f2)
cut -c1<<<${S^^}
```