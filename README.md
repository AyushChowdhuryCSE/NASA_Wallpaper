# 🌌 NASA APOD Wallpaper Setter

**Bring the cosmos to your desktop, every single day.**

This Python automation tool fetches NASA's [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/astropix.html) and sets it as your Windows desktop wallpaper. It also brings down the story behind the stars, saving the daily explanation to a text file for you to learn more about our universe.

## ✨ Features

- **Daily Updates**: Automatically fetches the latest image from NASA's API.
- **High-Resolution Support**: Preferentially downloads the HD version of images.
- **Smart Filtering**: intelligently handles days where the APOD is a video (skipping the wallpaper update but fetching the metadata).
- **Contextual Storytelling**: Saves the official NASA explanation to `story.txt` so you know what you're looking at.
- **Set & Forget**: Includes a batch script and automation steps for zero-touch daily updates.

## 🛠️ Prerequisites

- **OS**: Windows 10/11
- **Python**: Version 3.6 or higher
- **Internet Connection**: Required to reach `api.nasa.gov`.

## 🚀 Installation

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/nasa-wallpaper-setter.git
    cd nasa-wallpaper-setter
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

1.  **Get a NASA API Key**
    - Visit [api.nasa.gov](https://api.nasa.gov/).
    - Sign up (it's free and instant).
    - Copy your API Key.

2.  **Setup Environment Variables**
    - Create a file named `.env` in the project folder.
    - Add your API key to it like this:
      ```env
      NASA_API_KEY=YOUR_ACTUAL_API_KEY_HERE
      ```
    - (Optional) You can use `.env.example` as a template: simply copy it to `.env` and fill in your key.

## 🖥️ Usage

### Manual Run

You can run the script manually at any time to update your wallpaper immediately:

```bash
python main.py
```

### 🤖 Automatic Daily Updates

To have your wallpaper update automatically every day at 9:00 AM:

1.  **Open Command Prompt as Administrator**.
2.  **Register the Task**:
    Run the following command (update the path to match where you downloaded the project):
    ```cmd
    schtasks /create /tn "NASA Wallpaper Setter" /tr "E:\path\to\NASA_Wallpaper\run_wallpaper.bat" /sc daily /st 09:00
    ```
    _Note: The included automation setup ensures the task runs as soon as possible if you are offline at 9:00 AM._

## 📂 Project Structure

- `main.py`: The core logic for fetching data and setting the wallpaper.
- `requirements.txt`: Python package dependencies.
- `run_wallpaper.bat`: Wrapper script for the Windows Task Scheduler.
- `wallpaper.jpg`: The latest downloaded image (overwritten daily).
- `story.txt`: The explanation for the current image.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

_Powered by [NASA Open APIs](https://api.nasa.gov/)_ 🚀
