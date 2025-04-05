#Problem:
#You have a log file server.log with the following format:

#[INFO] 2025-04-05 12:30:45 Server started at port 8080
#[ERROR] 2025-04-05 12:31:01 Connection failed for user admin
#[INFO] 2025-04-05 12:32:15 Server health check passed
#[ERROR] 2025-04-05 12:33:45 Timeout while connecting to database
#[DEBUG] 2025-04-05 12:34:01 Debugging network issue
#[DEBUG] 2025-04-05 12:34:01 Debugging network issue

#Goal:
#Extract all error messages ([ERROR] lines), clean them to show only the timestamp and the message, and sort them by timestamp.

#Solution Using grep, awk, sed, and sort

#code

grep "\[ERROR\]" server.log | ##Filters lines containing [ERROR].
awk '{print $2, $3, $4, $5, $6, $7}' | ##Prints the date, time, and message (removing the [ERROR] part).
sed 's/\[ERROR\]//g' | ##Removes [ERROR] if it's still there (just for extra safety).
sort ##Sorts the logs by timestamp

