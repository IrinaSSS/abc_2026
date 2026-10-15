from datetime import datetime

def logger(message, log_file="app.log"):
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    line = f"{timestamp} | {message}"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    return line