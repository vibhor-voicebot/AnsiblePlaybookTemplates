echo "nodejs_ver=$1"
echo "vm_ip=$2"
cd my_terraform_module
rm -rf terraform/providers/registry.terraform.io/hashicorp/null
rm -rf terraform.tfstate
terraform init
terraform apply -auto-approve -var="nodejs_ver=$1" -var="vm_ip=$2"
cd ..
