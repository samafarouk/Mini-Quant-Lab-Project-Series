::: {align="center"}
# 💱 Python Currency Converter

**A beginner-friendly, menu-driven currency converter built with
Python.**

Convert between Egyptian Pounds (EGP), US Dollars (USD), and UAE Dirhams
using predefined exchange rates, then review your conversion history.

[Features](#-features) · [Getting Started](#-getting-started) · [How It
Works](#-how-it-works) · [Limitations](#-current-limitations) ·
[Roadmap](#-possible-improvements)

`<br>`{=html}

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Project-Completed%20Learning%20Project-2E8B57?style=for-the-badge)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-Not%20Specified-lightgrey?style=for-the-badge)

Last Updated: October 2024
:::

------------------------------------------------------------------------

## 📌 Overview

This project is a command-line currency converter created to practise
core Python programming concepts. Users select a source currency and a
target currency, enter an amount, and receive a converted value based on
a predefined exchange-rate dictionary. The program also stores
successful conversions in a session history.

> **Important:** The exchange rates are hard-coded example values, not
> live market rates. Update them before using the program for real-world
> financial calculations.

## ✨ Features

-   **Three currencies:** EGP, USD, and Dirham.
-   **Currency conversion:** Calculates a converted amount using a
    dictionary of currency-pair rates.
-   **Input checks:** Rejects currency names outside the supported list
    and amounts that are not entered as digits.
-   **Conversion history:** Displays successful conversions made during
    the current run.
-   **Menu-driven interface:** Convert, view history, or exit through a
    simple terminal menu.
-   **No third-party packages:** Uses standard Python functionality.

## 🧰 Tech Stack

  Tool                     Purpose
  ------------------------ ----------------------------------------------
  Python                   Core programming language
  Dictionaries             Store exchange rates by currency pair
  Functions                Separate conversion, history, and menu logic
  Lists and tuples         Store conversion records during the session
  Command-line interface   Collect user input and display results

## 🖥️ Example Workflow

When the program starts, it presents a menu similar to this:

``` text
Welcome to the Currency Converter!
Available currencies: EGP, USD, Dirham
Menu:
1. Convert Currency
2. View Conversion History
3. Exit
Choose an option:
```

Choose **1** to convert a currency, enter the source and target
currency, then provide an amount. Choose **2** to display the
conversions recorded during the current session, or **3** to exit.

The result is calculated using the rate stored for that currency pair.
For example, using the current hard-coded value in the script, `100 EGP`
converts to `3.20 USD`. This is only an illustration of the program's
logic, not a current exchange-rate quote.

## ⚙️ How It Works
### `convert_currency(amount, from_currency, to_currency, rates)`

Builds a tuple from the source and target currency, looks up that pair
in the rate dictionary, and multiplies the amount by the matching rate.
It returns `None` if the pair is missing.

### `show_history(history)`

Prints a message when no conversions have been recorded. Otherwise, it
loops through the session records and prints each conversion.

### `main()`

Runs the interactive menu, collects user input, checks the currency
names and amount format, calls the conversion function, records
successful conversions, and exits when the user selects option 3.


The program currently defines these pairs:

  Currency pair     Hard-coded rate
  --------------- -----------------
  EGP → USD                   0.032
  USD → EGP                   31.25
  EGP → Dirham                 0.12
  Dirham → EGP                 8.33
  USD → Dirham                 3.67
  Dirham → USD                 0.27

These values are fixed in the source code and is outdated as last edited was in october 2024. The program does not retrieve rates from
an external API.


## 📁 Project Structure

``` text
Mini-Quant-Lab-Project-Series/
├── Project.py
└── README.md
```

## ⚠️ Current Limitations

-   **Fixed exchange rates:** Rates are hard-coded and do not update
    automatically.
-   **Whole-number input only:** `amount.isdigit()` rejects decimal
    amounts such as `12.50` and negative numbers.
-   **Session-only history:** Conversion records are stored in memory
    and disappear when the program closes.
-   **Limited input normalization:** Currency names are case-sensitive,
    so users must enter `EGP`, `USD`, or `Dirham` exactly as prompted.
-   **No automated tests:** The repository currently does not include a
    test suite.

These are useful next steps for improving the project; they are not
features currently implemented.

## 🗺️ Possible Improvements

-   [ ] Accept decimal amounts and handle invalid numeric input safely.
-   [ ] Normalize currency input so lowercase entries are accepted.
-   [ ] Fetch current exchange rates from a reliable API.
-   [ ] Save conversion history to a CSV or JSON file.
-   [ ] Add automated tests for conversion calculations and input
    validation.
-   [ ] Add more currencies and a graphical user interface.

## 🎯 Learning Objectives

This project offers practice with:
-   Python functions and control flow
-   Dictionaries, lists, and tuples
-   User input and validation
-   Basic arithmetic and formatted output
-   Separating program tasks into reusable functions

## 👩‍💻 Author

**Sama Farouk**\
International Economics student building projects that connect
analytical thinking with practical technical skills.

Explore more work on [GitHub]([https://github.com/](https://github.com/samafarouk)) 


------------------------------------------------------------------------

::: {align="center"}
**If you found this project useful, feel free to ⭐ the repository!**
:::
