# PowerShell script to install Docker and start Solr as a Docker container on Windows Azure VM

# Step 1: Install Docker on the VM
$dockerInstallerUrl = "https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe"
$dockerInstallerPath = "$env:TEMP\DockerDesktopInstaller.exe"

# Download Docker installer
Invoke-WebRequest -Uri $dockerInstallerUrl -OutFile $dockerInstallerPath

# Install Docker
Start-Process -FilePath $dockerInstallerPath -ArgumentList '/quiet' -Wait

# Step 2: Start Solr as a Docker container
$solrContainerName = "my_solr"
$solrImageName = "solr:latest"
$solrContainerPort = "8983"

# Pull the Apache Solr Docker image
docker pull $solrImageName

# Run Apache Solr container
docker run -d -p $solrContainerPort:8983 --name $solrContainerName $solrImageName

# Wait for Apache Solr container to be ready
Start-Sleep -Seconds 10
while ((docker inspect -f '{{.State.Running}}' $solrContainerName) -ne 'True') {
    Start-Sleep -Seconds 5
}

# Output success message
Write-Output "Docker and Solr as a Docker container have been installed and started successfully."

