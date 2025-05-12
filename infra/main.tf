terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

# Provider for Storage Account (Azure subscription 1)
provider "azurerm" {
  features {}
  subscription_id = "3d8a9a8e-fe6c-4b1e-8379-0633545b8249"
  use_cli         = true
  alias           = "storage_sub"
}

# Provider for CDN Resources (Dev subscription)
provider "azurerm" {
  features {}
  subscription_id = "08508112-2820-4f03-bce3-23e30c0b80dc"
  use_cli         = true
  alias           = "cdn_sub"
}

# Get storage account from subscription 1
data "azurerm_resource_group" "bkRG" {
  provider = azurerm.storage_sub
  name     = "bkRG"
}

data "azurerm_storage_account" "bkcrcstorageacc" {
  provider            = azurerm.storage_sub
  name                = "bkcrcstorageacc"
  resource_group_name = data.azurerm_resource_group.bkRG.name
}

# Get CDN resources from Dev subscription
data "azurerm_resource_group" "cdn_rg" {
  provider = azurerm.cdn_sub
  name     = "MyResourceGroup"
}

data "azurerm_cdn_profile" "existing" {
  provider            = azurerm.cdn_sub
  name                = "MyCDNProfile"
  resource_group_name = data.azurerm_resource_group.cdn_rg.name
}

resource "azurerm_cdn_endpoint" "brookkassa" {
  provider            = azurerm.cdn_sub
  name                = "brookkassa"
  profile_name        = data.azurerm_cdn_profile.existing.name
  resource_group_name = data.azurerm_resource_group.cdn_rg.name
  location            = "global"
  is_https_allowed    = true
  is_http_allowed     = false

  origin {
    name      = "resume-storage"
    host_name = data.azurerm_storage_account.bkcrcstorageacc.primary_web_host
  }
}