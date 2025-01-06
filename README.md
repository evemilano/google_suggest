# Google Suggest Keywords Scraper

This Python script uses the Google Suggest API to extract related keywords for given search queries. It recursively expands the keyword list by using the related keywords from previous cycles as new input queries. 

The script allows users to input multiple initial queries, specify the desired language, and set the number of recursive cycles to run.

Features:
- Supports multiple initial queries as input.
- Fetches related keywords using the Google Suggest API.
- Recursively expands the list of keywords over a user-defined number of cycles.
- Saves the final list of keywords, including the initial queries, to a text file.
- Avoids duplicate queries to optimize HTTP requests.

Requirements:
- Python 3.6 or higher
- Libraries:
  - requests

Installation:
1. Clone this repository:
   git clone <repository-url>
   cd <repository-folder>

2. Install required dependencies:
   pip install requests

Usage:
1. Run the script:
   python <script_name>.py

2. Enter the required input when prompted:
   - Initial queries: Enter multiple search queries separated by commas (e.g., keyword1, keyword2).
   - Language: Enter the language code (e.g., en for English, it for Italian).
   - Number of cycles: Enter the number of recursive cycles to perform.

3. The script will fetch related keywords for each query, expanding the list recursively.

4. After execution, the final list of keywords will be saved in a file named related_keywords.txt in the same folder as the script.

Example:
Input:
Enter the initial queries (separated by commas): laptop, smartphone
Enter the language (e.g., it, en): en
Enter the number of cycles: 2

Output:
The final list of keywords will be saved in related_keywords.txt:
laptop
smartphone
best laptop
laptop deals
smartphone reviews
...

Notes:
- A 1-second delay is added between HTTP requests to comply with fair usage practices.
- The script ensures that duplicate queries are not processed multiple times.

License:
This project is licensed under the MIT License. See the LICENSE file for details.

Contribution:
Feel free to submit issues or pull requests to enhance this script.
