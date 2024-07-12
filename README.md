# WiFi Password Dumper
This Python script allows you to dump and retrieve saved WiFi passwords on a Windows machine using PowerShell commands. The script executes a PowerShell command to fetch WiFi profiles and their respective passwords, then formats and returns the results in a human-readable JSON format.

## Features
- Retrieves all saved WiFi profiles and their passwords.
- Outputs results in a well-formatted JSON format.
- Uses PowerShell commands to ensure accurate and comprehensive retrieval.

## Requirements
- Windows operating system.
- Python 3.x installed.
- PowerShell available and executable on the system.

## Usage
1. Clone the repository:
```bash
git clone https://github.com/yourusername/wifi-password-dumper.git
cd wifi-password-dumper
```
2. Run the script:
```bash
python wifi_password_dumper.py
```

## Example Output
```json
{
    "status": "success",
    "wifi_list": [
        {
            "wifi_name": "Network1",
            "wifi_password": "password123"
        },
        {
            "wifi_name": "Network2",
            "wifi_password": "password456"
        }
    ]
}
```

## Script Details
The script performs the following steps:

1. Define the PowerShell command:
   The PowerShell command used fetches WiFi profiles and their passwords.

2. Execute the PowerShell command:
   Uses the subprocess.run method to execute the PowerShell command.

3. Parse the output:
   Parses the output from the PowerShell command to extract WiFi names and passwords.

4. Format the results:
   Formats the results into a JSON object with an easy-to-read structure.

5. Return the JSON result:
   Returns the JSON-formatted string containing the status and list of WiFi profiles with their passwords.

## Error Handling
If the script fails to execute the PowerShell command or encounters any other issues, it returns a JSON object indicating the failure:
```json
{
    "status": "error",
    "message": "Failed to dump wifi passwords"
}
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
