# Enable WinRM (port 5985) inbound rule
az network nsg rule create --resource-group OpenAIGPTIAC --nsg-name AllowWinRM --name AllowWinRM --protocol Tcp --priority 100 --destination-port-range 5985 --access Allow --description "Allow inbound WinRM on port 5985"

# Enable SSH (port 22) inbound rule
az network nsg rule create --resource-group OpenAIGPTIAC --nsg-name sshallow --name AllowSSH --protocol Tcp --priority 101 --destination-port-range 22 --access Allow --description "Allow inbound SSH on port 22"

