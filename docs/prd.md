## Original Requirements
The boss has requested the creation of a Bitcoin wallet in C++. The wallet should have the same functionalities as Electrum, and it should be runnable with clear readme instructions.

## Product Goals
```python
[
    "Create a Bitcoin wallet in C++ with the same functionalities as Electrum",
    "Ensure the wallet is runnable on multiple platforms",
    "Provide clear readme instructions for users"
]
```

## User Stories
```python
[
    "As a user, I want to be able to create a new wallet so that I can start transacting in Bitcoin",
    "As a user, I want to be able to send and receive Bitcoin so that I can manage my digital assets",
    "As a user, I want to be able to check my balance and transaction history so that I can keep track of my Bitcoin",
    "As a user, I want to be able to backup and restore my wallet so that I don't lose my Bitcoin",
    "As a user, I want to be able to secure my wallet with a password so that my Bitcoin is safe"
]
```

## Competitive Analysis
```python
[
    "Electrum: A popular Bitcoin wallet with a simple interface and robust features. However, it is written in Python and may not perform as well as a C++ implementation",
    "Bitcoin Core: The original Bitcoin wallet, also written in C++. It is highly secure and stable, but lacks some of the user-friendly features of Electrum",
    "Armory: A secure Bitcoin wallet with advanced features like cold storage and multisig. However, it is complex and may be difficult for beginners to use",
    "Bitcoin Knots: A Bitcoin wallet with additional features not available in Bitcoin Core. However, it is not as widely used or well-documented as other wallets",
    "BitPay: A Bitcoin wallet with a focus on merchant services. It is not as feature-rich as other wallets for individual users"
]
```

## Competitive Quadrant Chart
```mermaid
quadrantChart
    title Bitcoin Wallet Competitive Analysis
    x-axis Low Usability --> High Usability
    y-axis Low Performance --> High Performance
    quadrant-1 High Usability, High Performance
    quadrant-2 Low Usability, High Performance
    quadrant-3 Low Usability, Low Performance
    quadrant-4 High Usability, Low Performance
    "Electrum": [0.7, 0.6]
    "Bitcoin Core": [0.5, 0.8]
    "Armory": [0.4, 0.9]
    "Bitcoin Knots": [0.6, 0.7]
    "BitPay": [0.8, 0.5]
    "Our Target Product": [0.7, 0.8]
```

## Requirement Analysis
The product should be a Bitcoin wallet implemented in C++. It should have the same functionalities as Electrum, including the ability to create a new wallet, send and receive Bitcoin, check balance and transaction history, backup and restore the wallet, and secure the wallet with a password. The wallet should be runnable on multiple platforms and come with clear readme instructions.

## Requirement Pool
```python
[
    ("Implement wallet creation feature", "P0"),
    ("Implement send and receive Bitcoin feature", "P0"),
    ("Implement balance and transaction history checking feature", "P0"),
    ("Implement wallet backup and restore feature", "P0"),
    ("Implement wallet password protection feature", "P0")
]
```

## UI Design draft
The wallet should have a simple and intuitive user interface. It should have a main screen showing the balance and transaction history, with options to send and receive Bitcoin. There should also be a settings page where users can backup and restore their wallet, and set a password for their wallet. The design should be clean and minimalist, with a focus on usability.

## Anything UNCLEAR
There are no unclear points.