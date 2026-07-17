import webbrowser
import urllib.parse
import time
from datetime import datetime

# Read dorks from file
with open("dorks.txt", "r") as file:
    dorks = [line.strip() for line in file if line.strip()]

# Create log file
with open("search_results.txt", "w", encoding="utf-8") as log:

    log.write("DAY 9 - SEARCH AUTOMATION LOG\n")
    log.write("=" * 60 + "\n\n")

    for count, dork in enumerate(dorks, start=1):

        # Encode the Google search query
        query = urllib.parse.quote(dork)
        url = f"https://www.google.com/search?q={query}"

        # Open in browser
        webbrowser.open_new_tab(url)

        # Current time
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Save to log
        log.write(f"Search {count}\n")
        log.write(f"Time : {current_time}\n")
        log.write(f"Dork : {dork}\n")
        log.write(f"URL  : {url}\n")
        log.write("Status : Opened Successfully\n")
        log.write("-" * 60 + "\n")

        print(f"{count}. Opened: {dork}")

        # Wait before opening next tab
        time.sleep(5)

print("\nAll searches completed.")
print("Log saved as search_results.txt")