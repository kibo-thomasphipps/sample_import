# Sample Local Project Import Test

This project demonstrates how to set up a local Python project with dependencies on local libraries.

## Setup Instructions

1. **Create a virtual environment** at the root of the project:

    ```bash
    python3 -m venv venv
    ```

2. **Activate the virtual environment**:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

3. **Install the local libraries**:

    ```bash
    pip install -e ./libs/shared1
    pip install -e ./libs/shared2
    ```

4. **Run the main script**:

    ```bash
    python projs/proj/bing.py
    ```

Remember to replace `python3` and `python` with the correct command for your Python 3 interpreter if it's named differently on your system.
