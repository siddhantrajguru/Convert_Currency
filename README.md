# 💱 Currency Converter

A simple and user-friendly desktop currency converter application built with Python and Tkinter.

## 🌟 Features

- 💵 Convert between 4 major currencies (USD, INR, EUR, GBP)
- 🖥️ Clean and intuitive graphical user interface
- ⚡ Real-time conversion calculations
- 📊 Static exchange rates for demonstration purposes
- 🚫 Input validation and error handling
- 🎨 Simple and responsive design

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Tkinter (usually comes pre-installed with Python)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/currency-converter.git
```
```
cd currency-converter
```

2. Run the application:
```bash
python currency_converter.py
```

## 💻 Usage

1. **Enter Amount**: Type the amount you want to convert
2. **Select From Currency**: Choose the source currency from the dropdown
3. **Select To Currency**: Choose the target currency from the dropdown
4. **Click Convert**: Press the "Convert" button to see the result

## 🌍 Supported Currencies

| Currency | Code | Symbol |
|----------|------|--------|
| US Dollar | USD | $ |
| Indian Rupee | INR | ₹ |
| Euro | EUR | € |
| British Pound | GBP | £ |

## 🔧 Technical Details

- **Language**: Python 3.x
- **GUI Framework**: Tkinter
- **Libraries Used**: 
  - `tkinter` - For GUI components
  - `ttk` - For themed widgets
  - `messagebox` - For error dialogs

## 📝 Code Structure

```
currency_converter.py
├── conversion_rates (dict) - Static exchange rates
├── convert_currency() - Main conversion logic
└── GUI components - Tkinter interface setup
```

## ⚠️ Important Notes

- 📊 **Static Rates**: This application uses static exchange rates for demonstration purposes
- 🔄 **Real-time Rates**: For production use, consider integrating with a live exchange rate API
- 💡 **Educational Purpose**: This project is designed for learning and demonstration
