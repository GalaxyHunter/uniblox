# Ecommerce Store Project

This is a simple Ecommerce Store project with features like adding items to a cart, checking out, applying discounts, and providing admin functionalities for generating discount codes and viewing statistics.

## Table of Contents
- [Requirements](#requirements)
- [Proposed Solution](#proposed-solution)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Frontend (Stretch Goal)](#frontend-stretch-goal)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

### Ecommerce Store
- Users can view and add items to their cart.
- Users can check out their items.

### Cart Functionality
- Users can add items to their cart.

### Discounts
- Every nth order gets a coupon code for a 10% discount.
- Validate if the discount code is valid before applying.

### Admin Functionalities
- Admins can generate discount codes if the condition is satisfied.
- Admins can view statistics.

## Proposed Solution

### Backend:

#### Data Structures:
- **Cart:** Store the items added by the user.
- **Orders:** Store successful orders.
- **Discount Codes:** Store generated discount codes and their usage status.

#### API Endpoints:

1. `/add-to-cart`: Add items to the user's cart.
   - Input: Product ID, Quantity
   - Logic: Update the cart structure.

2. `/checkout`: Checkout and apply discount if valid.
   - Input: User ID, Discount Code (if any)
   - Logic:
     - Calculate the total purchase amount.
     - Check if the discount code is valid and applicable.
     - Apply a 10% discount if valid.
     - Create an order entry in the "Orders" data structure.
   
3. `/admin/generate-discount`: Generate a discount code if criteria is met.
   - Input: Admin Token (for authentication)
   - Logic:
     - Check if the current order count is a multiple of 'n'.
     - If yes, generate a discount code and store it in the "Discount Codes" data structure.

4. `/admin/stats`: Get statistics.
   - Input: Admin Token (for authentication)
   - Output:
     - Count of items purchased.
     - Total purchase amount.
     - List of discount codes.
     - Total discount amount.

#### Flow:

- When an item is added to the cart, update the cart structure.
- On checkout, check for a valid discount code. If valid, apply a 10% discount.
- After every nth order, generate a discount code (using the admin API).
- The discount code can be used once before the next one becomes available on the next nth order.

### Frontend (Stretch Goal):
A simple UI where users can:

- View items
- Add items to their cart
- View their cart
- Checkout

An admin section where admins can:

- View and generate discount codes
- View statistics

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/GalaxyHunter/uniblox
