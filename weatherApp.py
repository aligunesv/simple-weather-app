# Import the Python GUI interface library.
import tkinter as tk

# Import the Python HTTP requests library.
import requests

# Define the API key to use
api_key = "api_key_in_here"

# Specify the city name from which weather information will be retrieved
city = "Istanbul"

# Defines the WeatherApp class derived from the tk.Frame class.
class WeatherApp(tk.Frame):

    # Defines the constructor method of the WeatherApp class.
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        #Allows the widget to be placed by wrapping the widget itself.
        self.pack()

        #Creates other widgets to be placed inside the widget.
        self.create_widgets()

    def create_widgets(self):

        #Creates the tk.Label widget.
        self.weather_label = tk.Label(self)
        self.weather_label.pack()

        #Creates the tk.Button widget and sets a command to call the refresh_weather() method.
        self.refresh_button = tk.Button(self, text="Refresh", command=self.refresh_weather)
        self.refresh_button.pack()

        #Creates the tk.Button widget and sets a command to close the application.
        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

        #Calls the function used to refresh the weather data.
        self.refresh_weather()

    def refresh_weather(self):

        # Generates the API URL used to retrieve weather data from the OpenWeatherMap API.
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # The requests library is used to get data from the API.
        response = requests.get(url)

        # The data received from the API is in JSON format, this line converts it into a Python dictionary.
        data = response.json()

        # The temperature (in kelvin) is subtracted from the data, converted to Celsius and rounded up.
        temp = round(data['main']['temp'] - 273.15, 1)

        # Moisture data is retrieved from the dictionary.
        humidity = data['main']['humidity']

        # Wind speed data is retrieved from the dictionary.
        wind_speed = data['wind']['speed']

        # The weather description is taken from the dictionary and the initials are capitalized.
        description = data['weather'][0]['description'].title()

        # Weather data is converted into a text string.
        weather_text = f"{temp}°C, {description}, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"

        # The generated text string is printed on the label in the GUI.
        self.weather_label.config(text=weather_text)

#Tkinter application is created.
root = tk.Tk()

# The WeatherApp widget is added to the Tkinter app.
app = WeatherApp(master=root)

# Tkinter uygulaması döngüsü başlatılır.
app.mainloop()


#https://github.com/aligunesv