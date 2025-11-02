# MCP Keyword Search Server

This is a simple MCP (Model Context Protocol) server built in Python using the `fastmcp` library.

The server provides a single tool, `search_file_for_keyword`, which allows an AI agent to search for a keyword within a specified text file on the server.

## Features
* **MCP Server:** A `fastmcp` server that listens for tool requests.
* **File Search Tool:** A tool named `search_file_for_keyword` that takes a `keyword` and `filename` as input.
* **Output:** Returns all lines from the file that contain the keyword, complete with line numbers.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the MCP Inspector to test:**
    This command will start the Inspector and tell it how to run your Python server.
    ```bash
    npx @modelcontextprotocol/inspector python server.py
    ```

5.  **Test in the Inspector:**
    * In the browser tab that opens, connect to the `stdio` server.
    * Go to the **Tools** tab and select `search_file_for_keyword`.
    * In the **Input** panel, use:
        * `keyword`: `"server"`
        * `filename`: `"sample_data.txt"`
    * Click **Run**.