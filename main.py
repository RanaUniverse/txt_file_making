from datetime import datetime, timezone, timedelta
from pathlib import Path

# Get current UTC time
now_time_gmt = datetime.now(timezone.utc)

# Convert to IST (UTC+5:30)
now_time_ind = now_time_gmt + timedelta(hours=5, minutes=30)

# Define the directory and filename
# directory = Path.home() / "Documents"

# Prepare the content to write
txt_variable = (
    "Hello, this is a new text file created using Python!\n"
    "You can write multiple lines by adding newline characters.\n"
    f"{now_time_ind}"
)
current_dir = Path.cwd()
new_dir = current_dir / "new_foler"

filename = "myfile.txt"

filepath = new_dir / filename

# Ensure the directory exists
new_dir.mkdir(parents=True, exist_ok=True)


# Write content to the file
filepath.write_text(txt_variable)

print(
    f"✅ File '{filename}' has been created and written successfully in '{current_dir}'."
)
