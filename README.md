# FEEDFORWARD 

### Backend installation and setup

```
cd Backend 
```
```
python -m venv venv 
```
```
venv/Scripts/activate
```
```
pip install -r requirements.txt

```

#### Run the backend
```
python run.py
```

### Frontend Installation and setup

#### In the root directory open terminal and type these commands:

```
cd Frontend
```
#### Install all the dependencies
```
npm install 
```
#### Run the frontend application
```
npm run dev
```


## Directory Structures
### Backend Directory
````
backend/
├── app/
│   ├── __init__.py                 # Initializes the Flask app, MongoDB connection, and Socket.IO
│   ├── models/                     # Directory for database schemas/models
│   │   ├── __init__.py             # Initializes the models module
│   │   ├── user.py                 # User schema and model logic
│   │   ├── food_listing.py         # Food listing schema and model logic
│   │   ├── request.py              # Request schema and model logic
│   │   ├── delivery.py             # Delivery schema and model logic
│   │   ├── feedback.py             # Feedback schema and model logic
│   ├── routes/                     # Directory for RESTful API routes
│   │   ├── __init__.py             # Initializes the routes module
│   │   ├── auth_routes.py          # Routes for authentication and user management
│   │   ├── food_routes.py          # Routes for food-related operations
│   │   ├── request_routes.py       # Routes for handling food requests
│   │   ├── delivery_routes.py      # Routes for delivery tracking
│   │   ├── feedback_routes.py      # Routes for feedback operations
│   ├── realtime/                   # Directory for real-time delivery tracking logic
│   │   ├── __init__.py             # Initializes the realtime module
│   │   ├── socket_events.py        # Socket.IO event handlers (tracking updates)
│   │   ├── location_service.py     # Helpers for geolocation and tracking
│   ├── utils/                      # Directory for helper utilities and functions
│   │   ├── __init__.py             # Initializes the utils module
│   │   ├── auth.py                 # Authentication and authorization logic
│   │   ├── helpers.py              # Miscellaneous helper functions
│   └── config.py                   # Configuration for the application
├── migrations/                     # Directory for database migrations (if applicable)
│   ├── versions/                   # Auto-generated migration scripts
│   └── env.py                      # Migration environment setup
├── .env                            # Environment variables (MongoDB URI, etc.)
├── requirements.txt                # List of dependencies for the project
├── run.py                          # Main entry point to run the Flask app

````
### Frontend Directory


````
frontend/
├── public/
│   ├── index.html                  # Main HTML file for the React app
│   ├── favicon.ico                 # Favicon for the application
│   ├── manifest.json               # Web app manifest
├── src/
│   ├── assets/                     # Directory for static assets (images, fonts, etc.)
│   ├── components/                 # Directory for reusable React components
│   │   ├── Header.js               # Header component
│   │   ├── Footer.js               # Footer component
│   │   ├── Map.js                  # Component for Leaflet map with live tracking
│   │   ├── LoginForm.js            # Login form component
│   │   ├── RegisterForm.js         # Registration form component
│   │   ├── FoodListingForm.js      # Form for listing surplus food
│   │   ├── FeedbackForm.js         # Form for feedback collection
│   ├── pages/                      # Directory for page-specific components
│   │   ├── HomePage.js             # Home page
│   │   ├── Dashboard.js            # User dashboard
│   │   ├── FoodListingPage.js      # Page for viewing available food listings
│   │   ├── DeliveryTrackingPage.js # Page for live delivery tracking
│   │   ├── FeedbackPage.js         # Page for feedback submission
│   ├── services/                   # API service functions
│   │   ├── authService.js          # Handles authentication API requests
│   │   ├── foodService.js          # Handles food-related API requests
│   │   ├── deliveryService.js      # Handles delivery tracking API requests
│   │   ├── feedbackService.js      # Handles feedback-related API requests
│   ├── store/                      # Redux store (if using Redux for state management)
│   │   ├── index.js                # Configures the Redux store
│   │   ├── authSlice.js            # Reducer for authentication state
│   │   ├── foodSlice.js            # Reducer for food-related state
│   │   ├── deliverySlice.js        # Reducer for delivery tracking state
│   │   ├── feedbackSlice.js        # Reducer for feedback state
│   ├── styles/                     # Directory for global and component-specific styles
│   │   ├── global.css              # Global styles for the app
│   │   ├── Map.module.css          # Styles for the Map component
│   ├── App.js                      # Main React component
│   ├── index.js                    # Entry point for the React application
├── package.json                    # NPM dependencies and scripts
├── .env                            # Environment variables (API endpoints, etc.)
````

