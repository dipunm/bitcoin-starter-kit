&nbsp;
\newpage

# Introduction
Welcome to the Bitcoin starter kit. This guide is designed to get you familiar with the core 
concepts of Bitcoin self custody and then build your knowledge as you create recovery plans, 
consider inheritance schemes, experiment with wallets, and become an expert at using and 
protecting your hard earned money.

We won’t focus on things like “what is money?” or “how much bitcoin makes me rich?”, this is 
purely a practical getting started guide for those who learn hands on.

A companion device has been developed to compliment this guide. In the spirit of openness and 
security, the starter kit adopted and created software built for the Badger2040, manufactured 
by Pimironi. The Badger2040 is a cheap electronic device (around £16 at the time of writing) 
with no wireless communication technologies and a built in e-ink display.

The companion device will walk you through the steps described in this guide, and will show
the results at every step. You are encouraged to follow along using paper and pencil to 
prove the integrity and accuracy of the product.

\newpage

## Motivation
### Education

Bitcoin provides an alternative to the traditional financial system backed by trust in 
governments and institutions, with a mathematically secured system using cryptography.

The purpose of this guide is to provide an understanding of the basic concepts and principles 
that are fundamental to Bitcoin’s security model, so that you can be confident about the 
security of your bitcoin, and the tools you use when handling it.

With the key word being “basic”, this guide will not make you some sort of crypto-expert, but 
it will provide the knowledge needed to secure your savings, and the techniques you can use to 
protect your wealth while simultaneously using it as a medium of exchange.

### Not your keys, not your coins
There are many companies and products that offer bitcoin as a service, that is, they will hold and look after bitcoin on your behalf, and provide web services and mobile applications that grant you the ability to see their liabilities to you.

Depending your own situation, many of the risks of using such services may be more or less of a concern to some than others, but one thing is for certain: these services re-introduce all of the risks associated with traditional finance, from censorship and political restrictions, to the risk of rehypothecation, bankruptcies or malpractice by the service provider.

It may seem complicated at first, but until you are managing your own keys and interacting directly with the Bitcoin network, you don’t have any bitcoin; you have bitcoin credit with a private company.

Credit is always at risk of being defaulted on, leaving you with nothing unless you are able to afford to use the legal system for a chance of some compensation. If you have bitcoin and not credit, then you will always be able to find buyers if you later wish to trade it for local currency or something else.

### The security of paper, mathematics and electronic devices

As an information system, Bitcoin security is not new or unique, but it is unfamiliar to many of us; yet as a monetary system, its security is of utmost importance. 

Just like a physical key, a Bitcoin private key is easy to copy - but in digital form, with the existence of malware and hackers, paired with a global internet, local wireless technologies such as bluetooth and even conspiracies about hardware being pre-compromised by three letter government agencies, the chances of others obtaining copies of your key becomes dangerously high.

The two things that are widely accepted by security experts as potential compromises when using electronic devices are:

Leakage of private or sensitive information via communication modules such as wifi, bluetooth{} or even USB.

Hardware that is unknowingly compromised, causing it to produce pre-determined or heavily biased random values in a way that could even be undetectable by anyone other than whoever compromised the device.

This means that we have to be careful about electronic devices and ideally not trust them to produce a random number, and not trust them to store or prevent leakage of our private keys.

This guide, along with the companion device, will help you to create private keys, mostly by hand, and using very limited hardware. We will use dice to ensure that our randomness is uncompromised, we will use lookup tables and worksheets to verify every step of the process, and we will take precautions to ensure data cannot be later leaked.