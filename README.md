# Time Zone Converter

A simple web application built using [Streamlit](https://streamlit.io/) that allows users to convert times between different time zones. This project is ideal for anyone needing to quickly and accurately convert time across global time zones.

## Features

- Convert any given date and time from one time zone to another.
- User-friendly interface powered by Streamlit.
- Supports all time zones available in `pytz`.

## Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/HarshShinde0/Time-Zone-Converter-Streamlit-App.git
    cd time-zone-converter
    ```

2. **Install the required Python packages**:

    Use the provided `requirements.txt` file to install the necessary dependencies.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**:
   - Open your web browser, and Streamlit will automatically navigate to the application.
   - Select the date, time, and time zones you want to convert from and to.
   - Click "Convert" to see the converted time.


## Example

Here’s a quick example of how to use the Time Zone Converter:

1. **Input**: Select `Aug 16, 2024, 03:00 AM` in `UTC`.
2. **Convert to**: `IST (Indian Standard Time)`.
3. **Output**: The converted time will be displayed as `Aug 16, 2024, 08:30 AM IST`.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. We welcome improvements and bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - For providing an awesome framework for building web apps.
- [pytz](https://pypi.org/project/pytz/) - For the comprehensive timezone support.

---
