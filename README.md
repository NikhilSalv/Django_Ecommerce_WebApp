# E-commerce Django Project Documentation

## Overview
This documentation provides an overview of an e-commerce Django project tailored for a clothing brand. The project encompasses several apps to manage various aspects of the e-commerce platform, including categories, products, payments, orders, and user management.

## Project Structure

<img width="586" alt="Screenshot 2024-02-05 at 01 05 27" src="https://github.com/NikhilSalv/PowerBI_Developer/assets/74225565/275f1396-9492-41f3-ac01-da9bc1f25ffb">

The project follows a typical Django project structure, consisting of multiple apps, each serving a specific functionality:
- **Category App:** Manages the categories of clothing products available on the platform.
- **Product App:** Handles the creation, management, and display of individual clothing products within different categories.
- **Payment App:** Integrates payment processing functionality, allowing users to make purchases securely.
- **Order App:** Facilitates the creation, tracking, and management of orders placed by users.
- **User App:** Manages user authentication, registration, profiles, and other user-related functionalities.

## Features
### Category Management
- Allows administrators to create, update, and delete product categories.
- Provides a user-friendly interface for browsing and selecting categories.

### Product Management
- Enables administrators to add new products, specifying details such as name, description, price, and images.
- Supports categorization of products under relevant categories.
- Includes features for product search, filtering, and sorting.
- Allows users to view product details and add products to their cart for purchase.

### Payment Processing
- Integrates with popular payment gateways to securely process transactions.
- Supports various payment methods, including credit/debit cards, PayPal, etc.
- Ensures secure transmission of payment information and compliance with PCI DSS standards.

### Order Management
- Tracks the status of orders, from placement to fulfillment.
- Provides order history for users to view past purchases and track current orders.
- Generates order invoices and shipping labels for efficient order processing.

### User Management
- Handles user authentication, including registration, login, and password reset.
- Manages user profiles, allowing users to update their information and view order history.
- Implements role-based access control (RBAC) to restrict access to certain functionalities based on user roles (e.g., admin, customer).

### API Testing with Swagger

<img width="1421" alt="Screenshot 2024-02-25 at 14 57 43" src="https://github.com/NikhilSalv/PowerBI_Developer/assets/74225565/38d1ae94-fb9d-453a-b7fb-7257897dde26">


- Utilizes Swagger tool to document and test APIs.
- Enables developers to collaborate effectively by providing a central location to explore API endpoints, their responses, and parameters.
- Facilitates frontend development by allowing frontend developers to understand and integrate with backend APIs seamlessly.
- 

## Technologies Used
- Django: Python-based web framework for building robust and scalable web applications.
- Django REST Framework (DRF): Provides powerful tools for building APIs and serializing data.
- HTML/CSS/JavaScript: Frontend development technologies for building responsive and interactive user interfaces.
- Bootstrap: Frontend framework for designing responsive and mobile-first websites.
- BrainTree API: Integration with payment gateways for secure payment processing.
- SQLite/PostgreSQL: Database management systems for storing and retrieving application data.

## Setup and Installation
To set up and run the e-commerce Django project locally, follow these steps:
1. Clone the project repository from GitHub.
2. Install Python and pip on your local machine if not already installed.
3. Create a virtual environment for the project and activate it.
4. Install project dependencies listed in the requirements.txt file.
5. Configure database settings in the project's settings.py file.
6. Run database migrations to create necessary tables in the database.
7. Start the Django development server and access the application in your web browser.

## Conclusion
This e-commerce Django project offers a comprehensive solution for managing an online clothing store, from product management to order processing and payment handling. With its modular architecture and user-friendly interface, the project provides a solid foundation for building a successful e-commerce platform for a clothing brand.

For any further assistance or inquiries, please refer to the project's documentation or contact the project maintainers.

