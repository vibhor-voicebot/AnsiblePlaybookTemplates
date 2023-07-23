provider "azurerm" {
  features {}
}


# Null Resource to execute the script on the existing VM
resource "null_resource" "update_nodejs" {

  # Connection settings to the existing VM
  connection {
    type        = "ssh"
    host        = var.vm_ip
    user        = "azureuser"  # Replace with your VM username
    private_key = file("~/.ssh/id_rsa")  # Replace with your SSH private key path
  }

  # Execute the script remotely on the VM
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get remove -y nodejs npm",
      "sudo apt-get install -y curl",  # Ensure curl is available
      "curl -sL https://deb.nodesource.com/setup_${var.nodejs_ver} | sudo -E bash -",
      "sudo apt-get install -y nodejs",
      "node --version"
    ]
  }
}

