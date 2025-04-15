
**Ansible-Automated ML Experimentation Environment**

Welcome to the Ansible-Automated ML Experimentation Environment! This project uses Ansible to set up a local machine learning (ML) sandbox with just one command. Designed for Windows users (via WSL2 Ubuntu), it installs essential ML tools—TensorFlow, PyTorch, Jupyter Notebook, and MLflow—in a clean Python virtual environment. Whether you’re a data scientist prototyping models, an MLOps engineer practicing automation, or a student diving into AI, this project makes starting your ML journey a breeze.

**Why This Project?**
Ever wanted to spin up an ML environment without wrestling with dependencies? This project automates the tedious setup, letting you focus on building models. It’s perfect for:

ML Enthusiasts: Quickly prototype models like MNIST classifiers.
MLOps Learners: Explore Infrastructure as Code (IaC) with Ansible.
Students/Engineers: Ensure reproducible, scalable ML workflows.
By combining Ansible’s automation with WSL2, it’s a lightweight solution that runs smoothly on Windows systems (like Intel i7, 16GB RAM setups) without needing a GPU.

**What’s Automated?**
System Dependencies: Installs Python, pip, curl, and unzip.
Virtual Environment: Creates an isolated Python environment.
ML Tools: Sets up TensorFlow, PyTorch, Jupyter Notebook, and MLflow.
Jupyter Notebook: Launches at http://localhost:8888 for interactive coding.
MLflow Server: Runs at http://localhost:5000 for experiment tracking.
Dataset Setup: Prepares a folder structure for datasets (e.g., MNIST).

**Quick Start**
Get up and running in minutes!

Clone the Repository:
bash

Copy
git clone https://github.com/Vamshikiran0301/ansible-ml-env.git
cd ansible-ml-env
Run the Ansible Playbook:
bash

Copy
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --ask-become-pass
Access the Tools:
Jupyter Notebook: http://localhost:8888
MLflow UI: http://localhost:5000
Note: Ensure WSL2 (Ubuntu) and Ansible are installed. See  for setup tips.

Project Structure
text

Copy
ansible-ml-env/
├── ansible/
│   ├── inventory.ini        # Ansible inventory file
│   ├── playbook.yml        # Main automation playbook
│   └── roles/              # Reusable Ansible roles
├── ml_env/
│   └── requirements.txt    # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # You’re here!
Prerequisites
OS: Windows 11 with WSL2 (Ubuntu 20.04+ recommended).
Tools: Ansible (sudo apt install ansible), Git.
Setup:
bash

Copy
# Install WSL2 on Windows
wsl --install
# Install Ansible in WSL2 Ubuntu
sudo apt update && sudo apt install ansible
Future Enhancements
I’m excited to grow this project! Planned features include:

Auto-downloading datasets (e.g., MNIST, CIFAR-10).
Dockerizing Jupyter and MLflow for portability.
Adding systemd services for persistent Jupyter/MLflow servers.
Supporting cloud deployment (e.g., AWS EC2 free tier).
Built With
Ansible – Automation engine.
TensorFlow & PyTorch – ML frameworks.
Jupyter Notebook – Interactive coding.
MLflow – Experiment tracking.

**MLflow Test Experiment**

This project includes a simple test script to make sure MLflow is working correctly.

The script:
- Generates a fake dataset using NumPy
- Trains a basic Linear Regression model using scikit-learn
- Logs the model, parameters, and mean squared error (MSE) to MLflow
- Lets you view the run in the MLflow UI at [http://localhost:5000](http://localhost:5000)

---

**How to Run It**

Make sure MLflow is already running:
```bash
/home/vmekala/ml_env/bin/mlflow ui --host 0.0.0.0 --port 5000

**Author**
Vamshi Mekala

MS, Information Systems & Operations Management

I’m a tech enthusiast hooked on AI infrastructure, DevOps, and making ML accessible through automation. Connect  When I’m not coding, you’ll find me exploring HPC clusters or chasing the latest in AI tech.

GitHub: Vamshikiran0301
LinkedIn: Vamshi Mekala (www.linkedin.com/vamshimekala1)

Contributing
Got ideas? Open an issue or submit a pull request! I’d love to collaborate and make this project even better.
