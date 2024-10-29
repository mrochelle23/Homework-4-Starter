# My Plants

My Plants is a web application designed to help users manage their plant collections. Users can add, edit, view details, and delete plants, as well as track harvest history and leave comments about their plants.

## Features

- Add new plants with details such as name, variety, photo URL, and planting date.
- View detailed information about each plant, including harvest history and comments.
- Edit existing plant details.
- Delete plants from the collection.
- Comment on plants for sharing experiences or notes.

## Technologies Used

- **HTML/CSS**: For the frontend layout and styling.
- **JavaScript**: For interactivity (confirmation dialogs).
- **Flask**: For backend development and routing.
- **MongoDB** (or any database of your choice): For storing plant data (not included in this example).

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

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any improvements or bug fixes.
