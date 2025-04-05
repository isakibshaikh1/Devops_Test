#Problem 
#Extract all error messages ([ERROR] lines) from a log file, clean them to show only the timestamp and the message, and sort them by timestamp.

import re
from datetime import datetime

# Class to process log files
class LogProcessor:
    def __init__(self, file_path):
        """
        Initializes the LogProcessor with the path to the log file.
        
        Args:
        file_path (str): The path to the log file (e.g., 'server.log').
        """
        self.file_path = file_path
        self.error_logs = []  # List to store error log lines

    def read_logs(self):
        """
        Reads the log file line by line and filters out lines containing [ERROR].
        This function only stores error logs in the error_logs list.
        """
        with open(self.file_path, 'r') as file:
            for line in file:
                if "[ERROR]" in line:  # Check if the line contains the [ERROR] tag
                    self.error_logs.append(line.strip())  # Clean whitespace and add to list

    def process_logs(self):
        """
        Processes the error logs to extract timestamps and error messages.
        
        - Uses regex to capture the timestamp and message separately.
        - Converts the timestamp into a datetime object for proper sorting.
        - Sorts the logs chronologically based on the timestamp.

        Returns:
        list: A sorted list of tuples where each tuple contains (timestamp, message).
        """
        processed_logs = []  # To store the final processed logs

        for log in self.error_logs:
            # Regex pattern to extract timestamp and message from the log line
            match = re.match(r"\[ERROR\]\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(.*)", log)
            if match:
                timestamp_str, message = match.groups()  # Extract matched groups
                # Convert the timestamp string into a datetime object for easy sorting
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                processed_logs.append((timestamp, message))  # Add to processed list

        # Sort the logs based on the timestamp (oldest first)
        processed_logs.sort(key=lambda x: x[0])
        return processed_logs

    def display_logs(self):
        """
        Displays the processed and sorted error logs in the format:
        'timestamp - error_message'
        """
        logs = self.process_logs()
        for timestamp, message in logs:
            print(f"{timestamp} - {message}")

# Example usage: This block runs when the script is executed directly.
if __name__ == "__main__":
    # Create an instance of LogProcessor with the log file path
    log_processor = LogProcessor("server.log")
    
    # Read the logs to filter out only error lines
    log_processor.read_logs()
    
    # Display the processed and sorted error logs
    log_processor.display_logs()
