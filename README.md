# 🖥️ Stock Price Prediction GUI App

## 🎯 Overview
This project is a **Desktop GUI Application** built using **Tkinter**, designed to demonstrate how Machine Learning models can be integrated into user-friendly interfaces. Users can input stock-related data and receive immediate predictions for the day's **highest** and **lowest** prices of selected banks.

> While the data is based on stock prices, this project mainly showcases the power of Python GUI development using **Tkinter**.

---

## 💡 Key Features

- 📊 **Interactive GUI**: Built entirely in **Tkinter** for seamless user interaction.
- 🧠 **Backend ML Model**: A simple Linear Regression model trained on historical bank stock prices.
- 🧾 **Database Integration**: Uses **MySQL** to store each prediction made via the app.
- 📤 **User Inputs**: Select bank name, enter date, previous close, and opening value.
- 📈 **Live Results**: Instantly see the predicted high and low values for the given input.

---

## 🧩 Tech Stack

| Component       | Technology       |
|----------------|------------------|
| GUI Framework   | Tkinter           |
| ML Model        | Linear Regression (Scikit-learn) |
| Data Handling   | Pandas, NumPy     |
| Database        | MySQL             |
| IDE Used        | Spyder            |

---

## 🖼️ Application Interface

### 🧑‍💼 Input Fields:
- Bank Name (Dropdown)
- Year, Month, Day
- Previous Close Price
- Opening Price

### 📤 Output:
- Displays **predicted High and Low values**
- Automatically saves inputs and results into MySQL

---

## 🔧 How It Works

1. **Startup**: Launches a Tkinter window with labeled input fields.
2. **Data Entry**: User selects/enters stock-related values.
3. **Prediction**: On clicking "Check High/Low", the model processes the input.
4. **Result Display**: Predicted High/Low prices are shown below the button.
5. **Database Logging**: The result and input data are saved into a MySQL table.

---

## 🔐 Sample Code Snippet

```python
b1 = Button(root, text="Check High/Low", bg="slateGray2", width=20, font=("bold",10), command=get_data)
b1.grid()
