# Supply Chain Network Optimization

A Python project that models and solves a supply chain network optimization problem using linear programming. The solution minimizes the overall cost of producing, transporting, and handling goods from plants through distribution centers (DCs) to customers using the PuLP library.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This project demonstrates the optimization of a three-stage supply chain network with:
- Multiple plants (factories)
- Multiple distribution centers (warehouses)
- Multiple customers (demand points)

The program determines the **optimal shipment quantities** between each stage to minimize total cost while satisfying demand, capacity, and flow balance constraints.

---

## Features

- Linear programming model built with PuLP.
- Flexible data setup for plants, DCs, and customers.
- Explicit cost breakdown for production, transportation, and handling.
- Constraint support for:
  - Plant and DC capacity
  - Customer demand fulfillment
  - DC inflow-outflow balance
- Clear output of solution status, total minimized cost, and all edge flows.

---

## Installation

1. Clone the repository or copy the script into your project directory.
2. Install required Python packages:

    ```
    pip install pandas pulp
    ```

---

## Usage

Edit the data sections (plant capacities, DC capacities, costs, and demands) as required and run the script:


**Output includes:**
- Optimization status (feasibility and optimality)
- Total minimized cost
- Flow from each plant to each DC
- Flow from each DC to each customer

---

## Model Details

- **Decision Variables:**
  - Flow from plants to DCs
  - Flow from DCs to customers

- **Objective Function:**
  - Minimize total cost = sum of production, transport (both legs), and handling costs

- **Constraints:**
  - Each plant’s total outflow ≤ plant capacity
  - Total inflow to each DC ≤ DC capacity
  - Total outflow from each DC = total inflow (flow conservation)
  - Each customer's demand must be fully satisfied

---

## Technologies Used

- **Python 3.x** – programming language
- **PuLP** – linear programming solver
- **pandas** – optional, for data processing and display

---

## Contributing

Contributions are welcome! Fork the repository, create a new branch, and submit a pull request with your changes. For significant updates, open an issue first to discuss your proposal.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
