from typing import List
import subprocess


def scan_wifi_linux() -> List[str]:
    try:
        result = subprocess.check_output(
            [
                "nmcli",
                "-t",
                "-f",
                "SSID,signal",
                "device",
                "wifi",
            ],
            encoding="utf-8",
        )
        networks = []
        for line in result.strip().split("\n"):
            ssid, signal = line.split(":")
            networks.append({"ssid": ssid, "signal": signal})
        return networks
    except Exception as e:
        print(f"Error: {e}")
        return []


print(scan_wifi_linux())
