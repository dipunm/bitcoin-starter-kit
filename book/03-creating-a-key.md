# Creating a key
Let's get straight into it. This chapter will focus on creating a private key. A private key is merely a large random number, however it is important that our number is created fairly using a scientifically sound method.

Handling such a large number with many digits is not easy, in fact it can be very easy to make mistakes when reading, writing, or typing it out. We will transform the number to a series of 12 words which will be much safer to record and easier to protect.

This transformation is not novel, it is a standard known as BIP-39. Storing your words in this standard form is good for a number of reasons:

- The standard has been formally proposed, amended, and published after deep thought and public discourse.
- Standards help to encourage consistent experiences across different products, applications and devices.
- Resources and information can be publicly found online, allowing you to verify the standard yourself.

Feel free to follow along with the instructions as you read this chapter. If you are planning to create a key that you can use securely, consider the following:

- Consider printing the provided instructions and templates before starting.
- Keep devices with microphones or cameras, including mobile phones and laptops, away or turned off.
- Keep your paperwork private and consider how you will destroy them securely after use.

## Creating a large random number
As simple as it sounds, coin flipping is sufficient enough to produce our large random number. In order to produce a number large enough, we will need to flip and record our result 128 times in a row.

Imagine recording all heads as the number 1, and all tails as the number 0. After 128 flips, we would have recorded a number in binary that looked like:

```
1001101101110111111011101000011111111110101010001000010101001011
```

... but 128 digits long.

This represents a number within a range larger than the number of **milliseconds** that has elapsed since the theorised **big bang** over 13.8 billion years ago: 1,152,921,504,606,846,976 times larger!

### Tips for flipping

#### There is no such thing as a weighted coin
Regardless of how smooth or rough a coin is, how heavy it is on one side, what material it was made or composed of, or how large or mis-shaped it is, a flipping coin will not favour one side over the other while in the air.

#### Don't let the coin hit the table
It has been theorised that the edge of a coin can cause a bias in the result of a coin flip favouring one side over the other if it hits a hard surface. It is known that a bad edge can affect the result of a coin spin, and it has been observed that some coin flips will spin on a hard surface before landing on a side. The best thing is to flip, catch and reveal. 

Don't worry about things like how your hand affects the results or whether you place the coin on the back of your hand before revealing or not. These factors may affect the outcome, but they don't introduce any biases in favour of one side vs the other.

#### Don't worry about repeating results
Humans are terrible at randomness, we are just wired to look for patterns. When we see the same result multiple times in a row, we feel uneasy because we internally expect "random" to mean "constantly changing", but really it means "unpredictable".

Don't re-flip or change your results just because it feels wrong, you'll only be reducing the randomness of the final answer.

#### Flip high and fair
I'm sure you know, if you make small, slow controlled flips, you can easily force the side you want to show up. That said, a reasonable height and a reasonable flip speed is more than enough to make the result completely unpredictable.

You don't need to overdo it, just aim to keep the coin in the air for at least 1 second, and ensure that the coin is flipping rapidly in the air. 

If you are not familiar with flipping a coin, you can roll it in your hands like a die and throw it into the air, allowing it to rotate in the air before landing onto a soft cusion.

### Recording the results
Hopefully by now, you are convinced that creating a massive, truly random number is easy enough to do without a computer.

We have provided a worksheet to help record your flips, you can record them as X's and O's, but something that will become very useful later on, is recording your flips in groups of 11 and then prefixing each group with an O. 

The reason why will be apparent when we get to transforming to plain words.

You may record heads as O and tails as X.

## Understanding the checksum
You should have noticed by now, that groups of 11 flips make 12 rows, but not completely. There is still space for 4 more results.

This space is reserved for the "checksum". A checksum is a short code that has been calculated from some data, for which we wish to provide integrity. The checksum can be calculated and re-calculated at any time and the result should always be the same.

_We'll call it a checksum-code for the rest of this section._

Our new large random number is our data, and if even a single digit of that data was changed after creating our checksum-code, the newly re-calculated checksum-code would no longer match our pre-calculated one.

This becomes useful for detecting typos and other human errors. When we enter our key(s) into a Bitcoin wallet, the software will extract and use the checksum-code to perform validation and provide a level of confidence that there hasn't been any funny business or typing errors before moving on.

One thing to note, is that calculating the checksum-code requires:

1. Using very complex mathematics (often delegated to some sort of computer)
2. Revealing your secret random number to whatever device is doing the calculation

We will deal with the checksum at the end, but for now we will focus on working exclusively on the first 11 rows.

## Transforming to plain words
Typically, this would be the last step after calculating the checksum, but doing it now will illustrate a point: the key really is made up by coin flips. Later when we calculate a checksum and complete the key, you will be able to see clearly how little of a change it made to your key

We will transform our flips in two steps:

1. Convert our X's and O's to three character "hexadecimal" codes
2. Use a table to look up and map our codes into words

### The three character hexadecimal codes

A quick primer on hexadecimal codes:

- We are most used to handling numbers using the numbers 0-9 for each digit, we call this representation "base 10".
- Computers often use binary to represent numbers, using only 0 or 1 for each digit, we call this "base 2".
- When dealing with large numbers, we often use the "base 16" representation, this is where each digit can be represented by one of the following characters: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
- An example of a hexadecimal code would be 3AF, which is equivalent to the number 943 in base 10.

To start, we can use our "hex lookup table". In groups of 4, we can map our X and O's to a single character, leaving us with 3 characters per row. As an example, a series such as <span class="underline">`OXOX`</span> <span class="underline">`XOXO`</span> <span class="underline">`XXOX`</span> would translate to <span class="underline">`5`</span> <span class="underline">`A`</span> <span class="underline">`D`</span>. 

This is where the prefixed O became useful, this prefix allowed us to split each row equally into 3 groups of 4 results for this exercise.

We can also calculate the code for the twelfth row, but with only 8 out of 12 results, we will not be able to calculate the last character of the code. There is not enough information to find the twelfth word just yet, but calculating the first two characters will still become useful later on.

### Mapping codes to words
The final step is to use the "mnemonic words lookup" book to convert each three digit code into a word. For example, `5 A D` would become `remember`.

You will be able to look up 11 of the 12 words that you need. The order of words are important, don't mix them up.

## Calculating the checksum and final word
In order to get our final word, we need to complete the last code, and in order to do that, we need to calculate the checksum.

Unfortunately, this step requires some sort of computer, and you may recall that we previously discussed how we cannot trust a computer to create a random number for us, **and** we cannot trust a computer to keep secrets and not leak them.

The random number is very precious, it is unique, newly discovered, never before seen, and central to our security. If anyone were to obtain this number, they could potentially discover and steal our bitcoin.

This is where we must make a calculated tradeoff. Fortunately, by generating our random number by hand, we only need to consider the risk of data leaks. As mentioned in the introduction, the companion device has no wireless transmitters that might leak sensitive data; however it does have a USB connector and persistent storage.

For the sake of brevity, We will focus on using the companion device to calculate the checksum, however to learn more about the risk factors of the device, read XXXX. To learn of some alternative ways to generate a checksum without this device, read XXXX.

### Using the companion device
In order to stay secure, we should power the device using a wall charger; this will prevent any data from being leaked through the data pins of the USB cable.

Once the device is powered on, select the XXX option.

TODO: Write code and document this.