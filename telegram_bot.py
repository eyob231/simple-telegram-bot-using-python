
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler

# Replace with your Google Maps API key (if needed)
GOOGLE_MAPS_API_KEY = 'YOUR_GOOGLE_MAPS_API_KEY'

# Dictionary to store building names, IDs, and coordinates
buildings = {
   1: {"name": "Building A - Library 1", "lat": 10.330831, "lng": 37.743157, "type": "building"},
    2: {"name": "Building B - Library 2", "lat": 10.330359, "lng": 37.744197, "type": "building"},
    3: {"name": "Building C - Cafeteria 1", "lat": 10.330280, "lng": 37.746255, "type": "building"},
    4:{"name": "Building D - Main Library", "lat": 10.330354, "lng": 37.745433, "type": "building"},
    5: {"name": "Male Dormitory 1", "lat": 10.3330, "lng": 37.7230, "type": "dormitory", "category": "male"},
    6: {"name": "Male Dormitory 2", "lat": 10.3340, "lng": 37.7240, "type": "dormitory", "category": "male"},
    7: {"name": "Female Dormitory 1", "lat": 10.3350, "lng": 37.7250, "type": "dormitory", "category": "female"},
    8: {"name": "Female Dormitory 2", "lat": 10.3360, "lng": 37.7260, "type": "dormitory", "category": "female"},
}

async def start(update: Update, context: CallbackContext) -> None:
    # Create a custom keyboard with two buttons
    keyboard = [
        [KeyboardButton("Current Location", request_location=True)],  # Button to request location
        ["Find Building"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)

async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    
    if text == 'Find Building':
        # Create a submenu with two options: Show Dormitory and Show Buildings
        keyboard = [
            [InlineKeyboardButton("Show Dormitory", callback_data="dormitory")],
            [InlineKeyboardButton("Show Buildings", callback_data="buildings")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('What would you like to find?', reply_markup=reply_markup)

async def handle_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    data = query.data

    if data == "dormitory":
        # Show options for Male and Female Dormitories
        keyboard = [
            [InlineKeyboardButton("Male Dormitory", callback_data="male_dormitory")],
            [InlineKeyboardButton("Female Dormitory", callback_data="female_dormitory")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Select a dormitory category:", reply_markup=reply_markup)
    elif data == "male_dormitory":
        # Filter and show only male dormitories
        male_dormitories = {id: building for id, building in buildings.items() if building.get("category") == "male"}
        if male_dormitories:
            # Create inline buttons for each male dormitory
            keyboard = [
                [InlineKeyboardButton(building["name"], url=f"https://www.google.com/maps?q={building['lat']},{building['lng']}")]
                for id, building in male_dormitories.items()
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.reply_text("Select a male dormitory:", reply_markup=reply_markup)
        else:
            await query.message.reply_text("No male dormitories found.")
    elif data == "female_dormitory":
        # Filter and show only female dormitories
        female_dormitories = {id: building for id, building in buildings.items() if building.get("category") == "female"}
        if female_dormitories:
            # Create inline buttons for each female dormitory
            keyboard = [
                [InlineKeyboardButton(building["name"], url=f"https://www.google.com/maps?q={building['lat']},{building['lng']}")]
                for id, building in female_dormitories.items()
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.reply_text("Select a female dormitory:", reply_markup=reply_markup)
        else:
            await query.message.reply_text("No female dormitories found.")
    elif data == "buildings":
        # Filter and show only buildings (non-dormitories)
        non_dormitories = {id: building for id, building in buildings.items() if building["type"] == "building"}
        if non_dormitories:
            # Create inline buttons for each building
            keyboard = [
                [InlineKeyboardButton(building["name"], url=f"https://www.google.com/maps?q={building['lat']},{building['lng']}")]
                for id, building in non_dormitories.items()
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.message.reply_text("Select a building:", reply_markup=reply_markup)
        else:
            await query.message.reply_text("No buildings found.")

async def handle_location(update: Update, context: CallbackContext) -> None:
    # Get the user's location
    location = update.message.location
    lat = location.latitude
    lng = location.longitude

    # Generate a Google Maps link for the user's location
    maps_url = f"https://www.google.com/maps?q={lat},{lng}"

    # Send the user their location on the map
    await update.message.reply_text(
        f"Your current location:\n{maps_url}",
        reply_markup=ReplyKeyboardRemove()  # Remove the custom keyboard
    )

def main() -> None:
    application = Application.builder().token('YOUR_TELEGRAM_BOT_TOKEN').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_handler(MessageHandler(filters.LOCATION, handle_location))  # Handle location updates
    application.add_handler(CallbackQueryHandler(handle_callback))  # Handle inline button clicks

    application.run_polling()

if __name__ == '__main__':
    main()
