# ECommerceBot
An End-to-End Ecommerce Bot leveraging LLMs


# Running the Project
```bash
conda create -n ecom -y python=3.10
```

```bash
conda activate ecom
```

```bash
pip install -r requirements.txt
```


## How to deploy on AWS
1. Create an EC2 instance
Run the following commands in the EC2 console

### Run the update commands
```bash
sudo apt-get update
sudo apt update -y
```

### Install these packages
```bash
sudo apt install git curl unzip tar make sudo vim wget -y
```

### Clone the repo
```bash
git clone https://github.com/prtk1729/ECommerceBot.git
```
### Install pip
```bash
sudo apt install python3-pip 
```

### Change Directory to the ECommerceBot and install the requirements
```bash
pip3 install -r requirements.txt --break-system-packages
```


