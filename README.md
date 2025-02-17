Telegram Bot: Campus Building and Dormitory Locator

This is a Telegram bot designed to help users locate buildings and dormitories on a university campus. The bot provides an interactive interface where users can request their current location, search for specific buildings, or filter dormitories by category (male or female). The bot uses inline keyboards and Google Maps links to make navigation easy and intuitive.
Features

    Current Location: Users can share their current location, and the bot will generate a Google Maps link for their coordinates.

    Find Buildings: Users can search for specific buildings on campus. The bot provides a list of buildings with direct links to their locations on Google Maps.

    Dormitory Search: Users can filter dormitories by category (male or female) and get direct links to their locations on Google Maps.

    Interactive Interface: The bot uses inline keyboards and buttons for a seamless user experience.

How It Works

    Start the Bot: Users start the bot by sending the /start command. The bot presents a custom keyboard with options to share their current location or search for buildings.

    Find Buildings: If the user selects "Find Building," the bot provides options to search for dormitories or general buildings.

    Dormitory Search: Users can filter dormitories by category (male or female) and select a specific dormitory to get its location on Google Maps.

    Building Search: Users can select a building from the list and get its location on Google Maps.

    Current Location: If the user shares their current location, the bot generates a Google Maps link for their coordinates.

Setup Instructions
Prerequisites

    Python 3.7 or higher: Ensure Python is installed on your system.

    Telegram Bot Token: Obtain a bot token from BotFather.

    Google Maps API Key (Optional): If you want to use additional Google Maps features, obtain an API key from the Google Cloud Console.

Installation

    Clone the repository:
    bash
    Copy

    git clone https://github.com/your-username/telegram-campus-bot.git
    cd telegram-campus-bot

    Install the required dependencies:
    bash
    Copy

    pip install python-telegram-bot

    Replace the placeholders in the code:

        Replace YOUR_TELEGRAM_BOT_TOKEN with your actual Telegram bot token.

        Replace YOUR_GOOGLE_MAPS_API_KEY with your Google Maps API key (if needed).

    Run the bot:
    bash
    Copy

    python bot.py

Code Structure

    bot.py: The main script containing the bot logic.

    buildings Dictionary: Stores building names, IDs, coordinates, and types (building or dormitory).

    Handlers:

        start: Handles the /start command and displays the initial keyboard.

        handle_message: Processes text messages and displays options for finding buildings or dormitories.

        handle_callback: Handles inline button clicks and filters buildings/dormitories based on user selection.

        handle_location: Processes the user's location and generates a Google Maps link.

Example Usage

    Start the bot:
    Copy

    /start

    Share your current location or select "Find Building."

    If you select "Find Building," choose between "Show Dormitory" or "Show Buildings."

    For dormitories, select "Male Dormitory" or "Female Dormitory" to see a list of options.

    Click on a building or dormitory to open its location on Google Maps.

Screenshots

Start Menu
Start menu with options to share location or find buildings.

Dormitory Selection
Selecting a dormitory category (male or female).

Building Location
Viewing a building's location on Google Maps.
Future Enhancements

    Add more building categories (e.g., academic buildings, recreational facilities).

    Integrate with a database for dynamic building data.

    Implement geolocation-based suggestions for nearby buildings.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
Contact

For questions or feedback, feel free to reach out:

    Email: eyobs573@gmail.com

    GitHub: eyob231

Enjoy using the Campus Building and Dormitory Locator bot! 🚀
