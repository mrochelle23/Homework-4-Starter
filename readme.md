# Plant Tracker App

The Plant Tracker App is a web application designed to help users manage and track their plants. It provides a simple interface to add, edit, and delete plant entries, as well as record harvesting details and view comments related to each plant.

## Features

- **Create a New Plant**: Add new plants with details such as name, variety, photo URL, and date planted.
- **View Plant Details**: View the details of each plant, including photo, variety, and planting date.
- **Edit Plant Details**: Edit the information of existing plants, such as their name, variety, and photo.
- **Track Harvesting**: Record harvested amounts and dates for each plant.
- **Comments**: Add comments to plants and view existing comments.
- **Delete Plants**: Remove plants from the tracker.

## Technologies Used

- **Flask**: A lightweight web framework for Python.
- **MongoDB**: NoSQL database used for storing plant data.
- **Jinja2**: Templating engine for dynamically generating HTML pages.
- **HTML/CSS/JavaScript**: For building the frontend interface.
- **Python**: The backend logic is implemented using Python.

## Project Structure

- **app.py**: The main Flask application file where routes and logic are handled.
- **templates/**: Directory containing HTML templates for rendering different views.
  - `base.html`: The base template containing common layout and styling.
  - `create.html`: The template for adding new plants.
  - `detail.html`: The template for viewing individual plant details.
  - `edit.html`: The template for editing plant details.
  - `plant_list.html`: The template displaying all plants.
  - `about.html`: A template displaying information about the app.
- **static/**: Directory containing static assets like CSS, JavaScript, and images.
  - `style.css`: The main stylesheet for the app.
  - `index.js`: JavaScript functions for confirming actions like deleting a plant.
- **requirements.txt**: A list of Python dependencies required to run the app.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mrochelle23/Homework-5-Starter.git
   cd Sprint
   ```

2. **Install dependencies:**
   If you're using Flask, create a virtual environment and install Flask:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install Flask
   ```

3. **Set up the database:**
   Ensure your MongoDB or chosen database is set up. Adjust the database connection settings in your Flask application as needed.

4. **Run the application:**
   ```bash
   flask run
   ```

   Visit `http://127.0.0.1:5000` in your web browser to access the application.

## Usage

- **Home Page**: View a list of all your plants and navigate to add a new plant.
- **Add Plant**: Fill out the form to add a new plant to your collection.
- **Plant Details**: Click on a plant to view its details, edit information, or delete it.
- **Harvesting**: Record the harvest details for your plants.
- **Comments**: Add comments to share your experiences with each plant.

