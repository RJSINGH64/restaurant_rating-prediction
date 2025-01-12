# 📊 Restaurant Rating Prediction 🚀

This project predicts restaurant ratings using the **Zomato Bengaluru Dataset** from Kaggle. The project implements a robust **MLOps Training Pipeline** in Python 3.12, designed to be modular, scalable, and production-ready.

---

## 🛠️ Step-by-Step Explanation

### 1. **Environment Setup**
- Python 3.12 environment was created to ensure compatibility and scalability.
- Installed all necessary libraries specified in `requirements.txt`.

### 2. **Project Folder Structure**

```plaintext
Restaurant-Rating-Prediction/
│
├── artifacts/                        # Contains all intermediate and final outputs
├── saved_models/                     # Production-ready models and transformers
│
├── Dockerfile                        # Docker image setup
├── docker-compose.yml                # Docker Compose for multi-container setup
│
├── .github/
│   └── workflows/
│       └── main.yaml                 # GitHub Actions CI/CD pipeline
│
├── src/
│   ├── components/                   # Core pipeline components
│   │   ├── data_ingestion.py         # Handles data collection
│   │   ├── data_validation.py        # Validates raw data
│   │   ├── data_transformation.py    # Prepares data for training
│   │   ├── model_training.py         # Trains the machine learning model
│   │   ├── model_evaluation.py       # Evaluates the model
│   │   └── model_pusher.py           # Pushes the trained model to deployment
│   │
│   ├── config.py                     # Configuration management and environment variables
│   ├── logger.py                     # Logging setup
│   ├── utils.py                      # Utility functions
│   ├── entity/                       # Data structures for pipeline
│   │   ├── config_entity.py          # Configuration-related entities
│   │   └── artifact_entity.py        # Artifacts generated by pipeline stages
│   │
│   ├── pipeline/                     # Pipeline automation
│   │   ├── training_pipeline.py      # Automates training workflow
│   │   └── batch_prediction.py       # Handles batch predictions
│   │
│   └── exceptions.py                 # Custom exception handling
│
├── app.py                            # Streamlit app for restaurant prediction
├── main.py                           # Entry point for training and predictions
├── data_dump.py                      # Dumps data into MongoDB Atlas
├── setup.py                          # Package setup for `src`
├── LICENSE                           # MIT License file
├── README.md                         # Project documentation
├── requirements.txt                  # Dependencies for the project
└── research.ipynb                    # Jupyter notebooks for initial analysis
```

---

## 🚀 Deployment to EC2 Using GitHub Actions

This project is deployed on an EC2 instance using Docker and GitHub Actions. Below are the steps for deployment:

### 1. **Create an EC2 Instance**
- Launch an EC2 instance with Amazon Linux 2 or Ubuntu.
- Configure security groups to allow HTTP (port 80) and SSH (port 22).
- Connect to the instance using SSH.

### 2. **Install Docker on EC2**
```bash
# Update packages
sudo apt update -y && sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add current user to the Docker group
sudo usermod -aG docker $USER
```

### 3. **Set Up GitHub Secrets**
Add the following secrets to your GitHub repository:
- `EC2_HOST`: The public IP or domain name of your EC2 instance.
- `EC2_USER`: The username for SSH (e.g., `ubuntu` for Ubuntu).
- `EC2_KEY`: The private key for accessing the EC2 instance.

### 4. **Configure GitHub Workflow**
Edit the `main.yaml` file under `.github/workflows/` with the following content:

```yaml
name: Deploy to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up SSH
        uses: webfactory/ssh-agent@v0.5.3
        with:
          ssh-private-key: ${{ secrets.EC2_KEY }}

      - name: Copy files to EC2
        run: |
          scp -o StrictHostKeyChecking=no -r * ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }}:/home/${{ secrets.EC2_USER }}/app

      - name: Deploy Docker on EC2
        run: |
          ssh -o StrictHostKeyChecking=no ${{ secrets.EC2_USER }}@${{ secrets.EC2_HOST }} << 'EOF'
          cd /home/${{ secrets.EC2_USER }}/app
          docker-compose down
          docker-compose up -d --build
          EOF
```

### 5. **Trigger Deployment**
- Push changes to the `main` branch.
- GitHub Actions will automatically deploy the latest version to your EC2 instance.

---

## 🌐 Access the Application
- Open your browser and navigate to the public IP or domain of your EC2 instance.
- You should see the Streamlit app running.

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.