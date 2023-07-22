# Enable WinRM service
Enable-PSRemoting -Force

# Allow WinRM through the Windows Firewall
Set-NetFirewallRule -Name "WINRM-HTTP-In-TCP" -RemoteAddress "Any" -Action Allow

