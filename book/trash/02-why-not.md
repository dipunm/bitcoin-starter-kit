# Why not ...?
Creating a Bitcoin wallet is much simpler than opening a bank account; you don't need to provide a stable home address that you've lived in for 6 months, you don't need a stable salary, and you don't need a valid passport to prove your citizenship. It also doesn't discriminate based on personality, ethnicity or gender, and is open 24hrs a day, 7 days a week.

Setting up a bitcoin wallet may feel daunting, and we may look for more familiar guides or tools to help speed up the process. This section will look deeper into the shortcuts we take, and why we might want to avoid doing so. Shortcuts are not necessarily bad, but without understanding the tradeoffs we are making, we are unable to forsee the negative outcomes of our actions.

> Note: read each subheading below as a continuation to the sentence: "Why not ... ?"

## Use a computer/mobile generated key
Cryptography is at the core of Bitcoin's security model, and its effectiveness is determined on our ability to produce a random number securely.

This is the same technology used to secure communications to protect online banking and encrypted messaging apps like WhatsApp. It even has military applications, having its first application as a tool to secure private communications in the 19th Century.

Our personal devices can produce reasonable random looking numbers, good enough to secure online interactions and to protect our personal communications and files from hackers.

High value individuals who might become a target, may find these devices do not provide enough protection from motivated attackers. Such attackers may compromise your devices beforehand or may be able to gather enough information to reproduce the random number produced by your device, and therefore reproduce your key.

Fortunately, it is easy to create real, reliably secure random numbers using just dice, pen and paper. Although you may not be targeted today, with the potential growth of value in bitcoin, it really _is_ worth the effort to create our own keys this way.

> To investigate the creation and protection of a Bitcoin private key is to indicate the desire for ownership and security of your bitcoin, and to use a computer generated key is to indicate not too much desire for security.

## Pick my own random words or numbers
Humans are bad at making random numbers. Our brains are wired for finding and adhering to patterns, it is how we learn, and how we survive.

To illustrate this, write out a random 20 digit number on paper. Once you have done so, continue reading the next chapter.

There are behavioural patterns that tend to show up when we attempt to create a random number:

- We often use sequential numbers, for example: ...2,3.. or even in reverse: ...5,4...
- Note: when we are working with words, we tend to pair words that we have heard together in mini clusters
- We tend to avoid the number 0
- We avoid repeating numbers such as ...,5,5,5...

Repeating numbers are very natural in random numbers, yet when we observe them, we become very uncomfortable. If we flip a coin and get the same result a few times in a row, we get the feeling that we must have unconciously forced this pattern either from the way we flip the coin, or something else. If we allow ourselves to omit certain results to remove these anomalies, we end up making our final result less random than before.

Look out for the patterns listed above in your 20 digit number. If we play again, but this time we try to hide these behavioural patterns, it should be obvious that we are now actively de-randomising our results. Hopefully this helps you to appreciate how helplessly predictable we are; and we are even worse when dealing with large numbers or long sequences.

Just like random numbers on a computer can be reproduced, the numbers and words that we choose can also be reproduced. 

A computer can effectively use a brute force technique, but will use a model of our common behavioural patterns to guide it; with the ability to make so many adjustments and guesses within seconds, it won't take long to find funds on a wallet that we chose to create this way.

## Make a digital copy of my key
After creating a secure private key, the next challenge is keeping it a secret. Computers are awful with secrets, especially if saved to disk and especially if stored in plain text.

Personal computers and devices take shortcuts, prioritising perception of speed over correctness; when we delete a file, a computer will "forget" where the file is stored, but not actually remove the data itself. Over time with usage, other data may be written over it, but until then, deleted data can be discovered and recovered _remotely_ via malware. With physical access to the device, forensic experts are able to discover data that was considered long gone.

If your device happened to been infected with malware, then simply entering the key into an application on the device can compromise it as the malware could monitor your key presses or search in memory for relevant information and then broadcast it over the internet. If your device is offline, it can save the information to disk without your knowledge with the intent to broadcast it when you connect to the internet later.

It may seem inconvenient to have to create and look after backups written on physical media such as paper or engraved steel (often used to protect against fire and floods), but the perceived convenience of a digital copy comes with **massive** risk. 

Abstaining from creating digital copies of your backup is a powerful way to provide a level of security that can be used to hold life savings, retirement funds, and inheritance money.

## Take a digital photo of my physical backup
Just like creating digital copies of your backup in plain text is a bad idea, so is creating digital images. It might seem like a way to hide information in plain sight; the text is represented as pixels, software can't read it... right?

Technologies like OCR can quickly scan and extract text from images and with the help of AI, the accuracy of extracting even badly hand written text can be pretty high.

Photos are simply no more secure than plain text; plain and simple.

While we are on the subject, ensure that there are no recording devices around when writing or reading your backups, and avoid ever reading them out loud; listening devices could be anywhere - mobile phones, smart speakers, smart TVs, all have microphones and are connected to the internet!

## Leave it to the exchanges
It can be tempting to leave funds on the exchange where you bought it from, they don't often advise you to withdraw, but they were trustworthy enough to be granted a banking licence, and they are regulated.

There have now been many examples of well trusted, well respected exchanges becoming insolvent, some as recent as in 2022. A large firm called FTX, which was working closely with regulators, became insolvent over night in late 2022 and customers with funds in their custody found themselves with no bitcoin and no compensation. Bitcoiners who had already taken self custody of their bitcoin were fine.

The mantra of "[not your keys, not your coins](#not-your-keys-not-your-coins)" is very important, and should not be taken lightly. When these incidents happen, they often start by freezing withdrawals and you are left to watch helplessly as events unfold with the bitcoin that you were owed, hanging in the balance.