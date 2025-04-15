 README.md – Starter Template
# Ansible-Automated ML Experimentation Environment
This project automates the setup of a machine learning experimentation environment using Ansible and WSL2 Ubuntu on Windows. It installs essential ML tools such as TensorFlow, PyTorch, Jupyter Notebook, and MLflow — all inside a Python virtual environment.
> Designed for data scientists, MLOps engineers, and students who want a one-command setup for local ML experimentation.
---
##  What's Automated
System dependencies (Python, pip, curl, unzip)  
Python virtual environment creation  
ML package installation: `tensorflow`, `torch`, `jupyter`, `mlflow`  
Jupyter Notebook launch on `localhost:8888`  
MLflow UI tracking server on `localhost:5000`  
Dataset folder structure and optional downloads (e.g., MNIST)
---
 Quick Start
1. Clone the Repository

Cmd: git clone https://github.com/Vamshikiran0301/ansible-ml-env.git
cd ansible-ml-env
2. Run the Playbook
CopyEdit
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --ask-become-pass


3. Access Tools in Browser
•	Jupyter Notebook: http://localhost:8888
•	MLflow UI: http://localhost:5000
________________________________________
 Project Structure
ansible-ml-env/
├── ansible/
│   ├── inventory.ini
│   ├── playbook.yml
│   └── roles/
├── ml_env/
│   └── requirements.txt
├── .gitignore
└── README.md
________________________________________
Why This Matters
This project demonstrates how Infrastructure as Code (IaC) can simplify and accelerate ML workflows. It’s ideal for:
•	ML enthusiasts who want to prototype quickly
•	MLOps students learning deployment practices
•	Engineers practicing reproducibility and automation
________________________________________




Author
Vamshi Mekala
MS - Information Systems & Operations Management
Passionate about AI Infrastructure, DevOps, and building automation for ML at scale.
________________________________________
Future Enhancements
•	Add support for dataset auto-downloads (MNIST, CIFAR-10, etc.)
•	Docker-based Jupyter + MLflow containerization
•	Systemd service setup for persistent notebook/MLflow servers
________________________________________
 Built With
•	Ansible
•	Jupyter
•	MLflow
•	TensorFlow
•	PyTorch
yaml
