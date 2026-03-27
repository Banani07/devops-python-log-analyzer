📘 DAY 1 DOCUMENTATION — Python Log Analyzer + Git Basics
🧠 1. What You Built (Big Picture)
You created a Log Analyzer Tool using Python.

👉 It:

Reads a log file

Identifies log types (ERROR, INFO)

Counts occurrences

Prints results

📄 What is a Log File?

https://images.openai.com/static-rsc-4/hA1lfYlaf73jZTOOUlj_Fh73w0sfNE5iW_k6HHOepTyPnrdcIr3Q8Uu4QJetwstAXiCIudzzV2PLrSEBm3jmAhfqgPPHjAIYYqIF1i8BZ4Fn26Eb2V8QcOlQAVfTs4w5Z0oQjskdkV4zvPhpHDZMuHcteRXpyboThcs1ZvzEFMj5YKE_M4a4K9BjzZQG8dIq?purpose=fullsize

https://images.openai.com/static-rsc-4/aU-viAibzfpY3a8UTaiU1d-FTqxTFhsVccpwEc7cQNJvqsik6uqEiWzAlPL4DkWOr5LOB5fBqoZ99iPEOFZaIyqsKDrmXM53JsT0h04xfhB5-Cq37vMd-wDzhxebQmA48-XbTSxw09vqdqhIcUW1OB5I6B_1aIjMv2fSPH2XcNTjwciXJhcHGxKRq1DIhfbH?purpose=fullsize

https://images.openai.com/static-rsc-4/XEi5Vq5jPxaPE_ckx7ffZ4MhQpxqeIzf85CY2MWo9Gi3qQ1VvzgGdQt_l2Q5xnbuW2hcvzziViCNe3yXMmaTw_OzjCwwFbDkOfM1YrTBmN2zCVwFgzwNpkH52Y0gc6UGl1ShZtAffEzb4NqI7bzMzqwFYCWuVWN26-Z_zPRa13YHHexL-YEAdDNzR7EangMh?purpose=fullsize
6
A log file is a file where systems write events like:

INFO: Server started
ERROR: Database failed
👉 In real DevOps:

Logs help debug failures

Logs help monitor systems

🐍 2. Python Script — Line by Line Explanation
Here is your script again:

with open("log.txt", "r") as file:
    error_count = 0
    info_count = 0
    total_lines = 0

    for line in file:
        total_lines += 1

        if "ERROR" in line:
            error_count += 1
        elif "INFO" in line:
            info_count += 1

print("Total lines:", total_lines)
print("ERROR:", error_count)
print("INFO:", info_count)
🔍 Understanding Step-by-Step
🔹 1. Opening the file
with open("log.txt", "r") as file:
👉 Means:

Open file named log.txt

"r" = read mode

with automatically closes file (good practice)

🔹 2. Variables (Counters)
error_count = 0
info_count = 0
total_lines = 0
👉 These store counts:

How many errors

How many info logs

Total lines

🔹 3. Loop through file
for line in file:
👉 Reads file line by line

Example:

Line 1 → INFO
Line 2 → ERROR
🔹 4. Count total lines
total_lines += 1
👉 Same as:

total_lines = total_lines + 1
🔹 5. Condition checking
if "ERROR" in line:
👉 Means:

If word ERROR is present → increase counter

🔹 6. Print output
print("ERROR:", error_count)
👉 Displays results in terminal

💡 Key Python Concepts You Learned
✔ File handling
✔ Loops (for)
✔ Conditions (if-elif)
✔ Variables
✔ String matching

👉 This is enough for basic DevOps scripting

⚙️ 3. Git & GitHub — Beginner Explanation
You used Git for version control.

👉 Tool: Git
👉 Platform: GitHub

📦 What is Git?
Git helps you:

Track changes in code

Save versions

Collaborate

🌐 What is GitHub?
GitHub is:

A cloud platform to store code

Share projects

🔁 4. Git Commands Explained (Very Important)
🔹 1. Initialize repository
git init
👉 Creates a .git folder
👉 Turns your folder into a Git project

🔹 2. Add files
git add .
👉 Adds all files to staging area

👉 OR better:

git add script.py log.txt
🔹 3. Commit changes
git commit -m "Day 1 - Log Analyzer Script"
👉 Saves your work with a message

Think:
📸 “Taking a snapshot of your code”

🔹 4. Create main branch
git branch -M main
👉 Renames branch to main

🔹 5. Connect to GitHub
git remote add origin <repo-url>
👉 Links your local project to GitHub

🔹 6. Push code
git push -u origin main
👉 Uploads code to GitHub

🔄 Git Workflow (Simple Flow)

https://images.openai.com/static-rsc-4/BHF1QUrB1xg0NGXyIkzlMTJ7teHq0yS3xB4BCiKaGGJIO7J3CRtR8fBCns3GXTw8i0p6IMVzR8EB88a_OaewD8VTvvzKXHoOnEOSdAY9tEThpzammKyUtT9hL57VpnOf_GI0voJR6pDetMo3k4zQqaBKy_XItl_ZppAQ6QKLt9_9yyuZXzZMAD3Xy19KHQtc?purpose=fullsize

https://images.openai.com/static-rsc-4/RkfRnEuEIQs5kWotqtLkFrmZD1SsWIuTeOeiD6CCV-JAhZv6wu_67uV9KoUgKIuqZPT6eaVaOHcB1R3Ti3YQ4mNzIDm5UWwnXxuqg_KHr4pNB_bWPIs9o3vwg8Ogr-1uye4KMR7TIZ_pxcEJf4h-6agt_ORPxMUUB_7mcIoMzXRniR7a2es03qIc8Ew5MBCr?purpose=fullsize

https://images.openai.com/static-rsc-4/EHFD4wjGjSixflnZpa7Qg2XzKg9KzvweYH6Y1RUBOYBsFv33I3m3RGZd2iLnce-ymkMFVn_EKDtiGWNX97AIZN0LX0v7U2oNdFepb_-tyPoIj0xWIJenEQTEEvVTCSx5SeyDycvqwZ1e7wCKSY3L9DWl5SuchNeUjUiSm0CDfcm5IjbP4j20jgyLNYedYLTL?purpose=fullsize
6
👉 Flow:

Code → git add → git commit → git push → GitHub
❗ 5. Mistakes You Faced (And Learned)
✔ Python not installed
👉 Fixed by installing Python

✔ Script not opening
👉 Learned to run via terminal

✔ Git index.lock error
👉 Learned how Git locking works

✔ Wrong git add (system files)
👉 Learned correct file handling

🎯 6. What You Achieved (Day 1 Summary)
By end of Day 1:

✅ Wrote Python script
✅ Understood file handling
✅ Used Git commands
✅ Pushed code to GitHub
✅ Debugged real issues

💼 7. How to Explain in Interview
Say:

“I created a Python script to analyze log files by counting error and info messages. I used Git for version control and pushed the project to GitHub.”

👉 Simple + clear + impactful

