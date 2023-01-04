&nbsp;
\newpage

# Welcome to the Bitcoin starter kit!
This guide is designed to introduce you to the core concepts of Bitcoin self custody and then build your knowledge as you progress through the various sections. This guide may be useful in a variety of ways, providing educational and interesting information and serving as a practical step-by-step guide.

We will cover topics such as:

- Assessing and applying the appropriate level of security for your needs.
- Exploring safely, avoiding potential security breaches and unexpected compromises.
- Managing and utilising your keys securely.
- Maintaining the safety and security of your bitcoin over time.
- Taking corrective and preventative measures after an incident.
- Future proofing with considerations for disaster recovery and inheritance setups.

_When getting started, it makes sense to use the different Bitcoin related apps, services and tools that interest you; play with them, and get a feel for what Bitcoin can do for you. It is NOT necessary to learn every aspect of this guide before exploring Bitcoin; instead, as you broaden your understanding, you can take the steps required to improve the security of your balances as you see fit._

You will get the most from this guide when you decide to start _saving_ with bitcoin. There will never be more than 21 million bitcoin in the world, its supply cannot be controlled or manipulated by any government or institution, and it has no limits or restrictions imposed by political agendas. We often find that, for these reasons, learning how to save and protect your bitcoin becomes more important over time, especially as others around you start to understand, appreciate and value bitcoin too.

To complement this guide, we have developed a companion device composed of custom software paired with the Badger2040: a cheap electronic device manufactured by Pimironi in the UK.

- The Badger2040 costs around £16 (at the time of writing).
- It is a simple, secure device that is easy to use. 
- It has no wireless transmitters that might leak sensitive data.
- It is pre-built with buttons and a screen, so it requires no electronic wiring or assembly.

Some sections are designed to be thought provoking. We will discuss technical vulnerabilities and how to safely navigate and avoid security breaches and unexpected compromises, and summarise by offerering practical, non-technical solutions that anyone can easily follow. 

While some of the threats we discuss may seem unlikely, take the time to consider whether it is really worth the convenience to overlook them; now and into the future. Even if you choose convenience based on your current circumstances, it is always beneficial to understand the risks you are taking and how you might improve your situation in the future if your circumstances change.

## Objectives
### Educate
Bitcoin provides an alternative to the traditional financial system and can be used for commerce and other financial transactions. Unlike traditional financial systems, which are typically backed by trust in governments and institutions, Bitcoin uses a mathematically secured system called cryptography.

Although this might sound complex, we don't need to understand the all complex mathematics deeply to create a secure wallet. In fact we really only need to worry about **creating large random numbers** and **keeping it secret**. This is the basic principles of "private key" security and will be the main topic of this guide.

This guide will explore the techniques we can use to secure our bitcoin and the tradeoffs we make when using the various types of applications and devices that are available to help us. By gaining the necessary knowledge, you can easily apply the appropriate amount of security for your unique needs.

We will also explore the ways we maintain our security, how we can identify mistakes and warning signs, and the steps we can take to restore security in a timely manner before anyone can take advantage if we ever do compromise it.

The thought of having to learn something novel can be offputting at first, but it is easy to forget how many years we have spent learning about traditional money and yet how little control we have of it. The hope is that in the years to come, the information presented here will become common sense as we come to appreciate the power of controlling our own financial assets.

### Empower safe experimentation
Over time, you will discover applications, tools and services that you can use to utilise your bitcoin in different ways. You should be free to experiment with them, but it helps to have a good level of knowledge to prevent you from falling for scams or from losing your bitcoin early on.

Similarly to how banks innovate with debit cards and financial services, the open market is also innovating with Bitcoin. For example, some wallets connect you to a technology similar to the Visa and Mastercard networks in that it enables instant payments and can reduce the cost per transaction, but with a key difference; it is a technology that does not introduce central trusted parties who could be compelled to seize or confiscate your bitcoin.

These innovations do not come without their tradeoffs however; some wallets require the private keys that protect the bitcoin you keep on the wallet to be on an internet connected personal electronic device such as a mobile phone or desktop computer. The information in this guide will not only help you to understand the tradeoffs that come with these innovations, but it will help you to assess them critically and exercise an appropriate level of caution before using them.

### Practice
This guide is not purely theoretical. We will walk you through creating your first private key, you will learn practical ways to protect your keys, and the companion device will aid you in performing some of the mathematically complex tasks along the way.

This guide can be used again and again as a reference, or as a tutorial, to help you to create wallets for different purposes and for different situations. If you wish to really internalise the information and be able to work with bitcoin as if it were second nature to you, practice makes perfect.

## Not your keys, not your coins
_This section will explore investment products and services for comparison purposes. Keep in mind, that this information is for educational purposes only and should not be taken as financial advice. You should do your own research and seek professional financial advice before making any investment decisions._

There are many companies and products that offer bitcoin as a service; that is, they offer to hold and protect bitcoin that you own on your behalf, similar to depositing money in a bank. With such services available to use, often for free too, what is the point of securing your bitcoin by yourself?

These companies and products often provide web services and mobile applications that allow you to access information about your bitcoin deposit, but these companies may not have the actual bitcoin to back the balance on your account, and they can default on your bitcoin deposit at any time.

Some commonly used products are:

- **Exchanges:** where you can trade local currency for Bitcoin and possibly other digital assets.
- **Interest accounts:** where you custody your funds with a company who promises to pay you interest like a bank account.
- **Trading platforms:** where you can manage sometimes automate buys and sells based on market conditions.

Using these types of bitcoin services will reintroduce risks that are associated with traditional finance, such as censorship, political involvement and intervention, and the risk of rehypothecation, bankruptcies, or malpractice by the service provider. These risks may be perceived differently by different individuals depending on their personal situation, but it is important to carefully understand these risks before using these services.

Until you are managing your own keys and interacting directly with the Bitcoin network, you may legally own it, but **you don’t _have_ the bitcoin**.

### An analogy
Imagine you buy a brand new car from a dealership and you decide to have the dealership store it in their garage for safekeeping. One day you go to pick up your car and the dealership tells you that they no longer have it. They claim that they were storing it in a warehouse that caught fire and all of the cars inside were destroyed; also that you are not due any compensation; there was no insurance, no legal protections, and the liability was all yours.

You must now rely on the legal system to fight for a favourable resolution, and of course you have a better chance of this if you can afford good representation or if you know important people in high places. The odds are usually unfairly stacked against the typical individual.

This is the very risk you take when you use custodial services. Upon a default of an asset such as bitcoin, not backed by nor contingent on governments, there is little chance of obtaining recourse or compensation mandated via regulation; there is much less chance of obtaining it in bitcoin or something equivalent in value.

### Bitcoin vs trackers
Some custodians do not allow you to withdraw bitcoin, they are typically trading or investment platforms that only allow you to withdraw your national currency. These companies merely provide to you a promise that tracks the price of bitcoin, a promise that may not be backed by it at all.

You may find that they have higher spreads, higher fees, or that they adjust their fees after you have locked in. To take funds out of the platform, you must first convert the asset to your national currency and you will find that as a traditional financial product, it is subject to the rates, fees and terms set by the custodial service provider.

You are not able to participate in the free market, and you are not able to find better rates, because you are not buying bitcoin. These companies offer an investment vehicle, that merely tracks the price of bitcoin.

Some platforms offer ETFs (exchange-traded funds). Although these are also investment vehicles, they may be traded on the stock market, and are usually scrutinized and approved before becoming available to ensure that they meet certain requirements for pricing, valuation, and reporting. Despite this, the same risks as before apply and due diligence must be taken to ensure all the risks are evaluated before investing in general.

_It is probably worth repeating here, that this information is for educational purposes only, is not financial advice and does not endorse any particular financial product._

## The other hidden risks of trusting a custodian
Custodians are required to hold a large amount of personal and financial information about their clients, including names, addresses, and transaction histories. This is often required due to regulations implemented across the globe, such as AML (anti money laundering) and KYC (know your customer).

These regulations require custodians to collect details and verify the identity of their clients and monitor their transactions for any suspicious activity; of course, different countries implement and enforce these regulations to varying degrees. The process of collecting and storing this information increases the risk of data leaks, where personal and financial information about clients may be accessed by unauthorized parties and results in identity theft or financial fraud.

A custodian may also be subject to pressure from governments or other powerful actors to act in their interests rather than in the best interests of their clients. Many countries carry the risk of government overreach, and custodians may be required to disclose client information or freeze assets at the request of government authorities without requesting your consent, and without you ever being charged of any crime beforehand.

In some cases, this can go beyond traditional financial regulations, such as the case in Canada, early 2022, where the Emergencies Act was invoked and used to freeze the bank accounts, donations, and Bitcoin related exchange accounts of individuals involved in protests relating to covid mandates, without due process. This was done in an attempt to stamp out the protest as a first resort, when other countries had already started relaxing theor mandates and a goal of the protest was to discuss the same for Canada.

Most people think of national currency as physical cash and do not consider the money in our bank accounts; yet most money exists only in digital form in bank accounts. Money should not have inherent features that allow it to be used to manipulate or coerce individuals or groups in order to achieve certain political or other objectives, yet banks have the ability to fully control our money, deterred only by law and regulations, and influenced by politics.

The same is true of custodians holding our bitcoin. Taking custody of your own bitcoin is akin to holding cash in your back pocket or even in a safe, all while remaining in digital form.

## Understanding the security of paper, mathematics and electronic devices
As briefly mentioned in the [Objectives](#objectives) section, bitcoin's security can usually be boiled down to two things:

1. Create a sufficiently large random number.
2. Keep that number private and hidden.

As an information system, Bitcoin security is not new or unique, but it is unfamiliar to many of us; yet as a monetary system, its security is of utmost importance.

Just like a physical key, a Bitcoin private key is easy to copy if exposed - but in digital form, the chances of others obtaining copies of your key becomes dangerously high due to the existence of malware and hackers, paired with a global internet and local wireless technologies such as wifi and bluetooth.

Although not often spoken about, intelligence agencies such as the CIA are a big threat to information security; not because they are targeting you, but rather because they have been known to insert backdoors into electronic hardware and software in collaboration with hardware manufacturers and developers in secret. This is not a theory, fiction, nor a conspiracy; it is publicly available information. Although we know this much, we have learned that intelligence agencies are good at working in secrecy and we simply cannot know how compromised our devices may or may not be.

The two things that are widely accepted by security experts as potential compromises when using electronic devices are:

1. Data of private or sensitive information can be leaked via communication modules such as wifi, bluetooth or even USB.
2. Hardware can be unknowingly compromised, causing it to produce pre-determined or heavily biased random values in a way that could even be undetectable by anyone other than whoever compromised the device.

This means that we have to be careful about electronic devices. We should **not** trust them to produce a random number, and we should **expect** them to store and attempt to leak all information, including our private keys, without our consent.

Electronic devices provide us with convenience, but when it comes to real security, they make performing proper due diligence and vetting much more difficult.

In this guide, we will explore in more detail how to produce random numbers securely without a computer, and we will explore the ways computers can leak sensitive information and how to prevent it.