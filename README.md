# End-to-End Red Wine Quality Prediction Using Machine Learning

## Table of Contents
1. [Introduction](#introduction)
2. [Installation Instructions](#installation-instructions)
3. [Resources](#resources)
4. [License](#license)
5. [Workflows](#workflows)
6. [How to Run](#how-to-run)
7. [AWS CICD Deployment with GitHub Actions](#aws-cicd-deployment-with-github-actions)
    - [EC2 and Docker Setup](#ec2-and-docker-setup)
8. [Conclusion](#conclusion)
9. [About Author](#about-author)

## Introduction
Welcome to the **End-to-End Red Wine Quality Prediction** project. The goal of this project is to develop a comprehensive machine learning pipeline to predict the quality of red wine based on various chemical properties. This project is divided into several components, including data ingestion, validation, transformation, model training, evaluation, and deployment.

### Key Features:
- **Data Ingestion**: Collects and processes raw data for use in the model.
- **Data Validation**: Ensures that the data is accurate and consistent.
- **Data Transformation**: Transforms the data into a suitable format for modeling.
- **Model Training**: Utilizes a Random Forest classifier to train the model.
- **Model Evaluation**: Assesses the model's performance using metrics like accuracy.
- **Prediction Pipeline**: Integrates the model into a pipeline for making predictions.
- **Deployment**: Deploys the model using AWS CICD and GitHub Actions.

The Random Forest classifier was chosen for its robustness and ability to handle the complexity of the dataset. The model achieved an accuracy of approximately 87%, indicating its effectiveness in predicting wine quality.

This project not only focuses on building a high-accuracy model but also emphasizes the importance of a streamlined workflow and deployment process. By leveraging AWS CICD and GitHub Actions, the project ensures that the model can be efficiently deployed and maintained.

## Installation Instructions
To get started with this project, follow the steps below:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ZeeshanML/End-to-End-Red-Wine-Quality-Prediction-Project.git
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python3 -m venv venv
    ```

    ```bash
    source venv/bin/activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Resources
- **Dataset**: [Red Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset)
- **License**: [MIT License](LICENSE)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Workflows
### Configuration Updates
- **Update `config.yaml`**: Modify configuration parameters as needed.
- **Update `schema.yaml`**: Define the schema for data validation.
- **Update `params.yaml`**: Set parameters for model training and evaluation.
- **Update the entity**: Reflect the data structure.
- **Update the configuration manager in `src/config`**: Manage configurations.
- **Update the components**: Ensure all components are up to date.
- **Update the pipeline**: Integrate all components.
- **Update `main.py`**: Orchestrate pipeline execution.
- **Update `app.py`**: Create a user interface for predictions.

## How to Run
Follow these steps to run the project:

1. **Run the application**:
    ```bash
    python app.py
    ```
2. **Access the application**: Open your local host at `0.0.0.0:8080`.

## AWS CICD Deployment with GitHub Actions
1. **Login to AWS Console**.
2. **Create IAM User** with the following policies:
    - `AmazonEC2ContainerRegistryFullAccess`
    - `AmazonEC2FullAccess`
3. **Create ECR Repository**:
    - Save the URI

### EC2 and Docker Setup
1. **Create EC2 Machine (Ubuntu)**
2. **Install Docker on EC2**:
    ```bash
    # Optional
    sudo apt-get update -y
    sudo apt-get upgrade
    # Required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```
3. **Configure EC2 as Self-Hosted Runner**:
    - Go to `Settings > Actions > Runners > New self-hosted runner`.
    - Choose OS and execute the provided commands.
4. **Setup GitHub Secrets**:
    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `AWS_REGION`
    - `AWS_ECR_LOGIN_URI`
    - `ECR_REPOSITORY_NAME`

## Conclusion

This project demonstrates an end-to-end machine learning pipeline for predicting the quality of red wine. It encompasses data processing, model development, and deployment using AWS CICD. The Random Forest classifier achieved an accuracy of around 87%, highlighting the model's effectiveness in predicting wine quality.


## About Author

- **Name**: Zeeshan Latif
- **Email**: [zeeshanlatif.work@gmail.com](mailto:zeeshanlatif.work@gmail.com)
- **Professional Links**:
    - [Kaggle](https://www.kaggle.com/zeeshanlatif)
    - [LinkedIn](https://www.linkedin.com/in/zeeshan-latif-2962211b1)
    - [GitHub](https://github.com/ZeeshanML)
- **Project Repository**: [GitHub Repo](https://github.com/ZeeshanML/End-to-End-Red-Wine-Quality-Prediction-Project)
