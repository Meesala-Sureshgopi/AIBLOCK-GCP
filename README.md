# AIBLOCK-GCP
Implementation of an IEEE conference paper **"[AIBLOCK: Blockchain-based Lightweight Framework for Serverless Computing using AI](https://ieeexplore.ieee.org/document/9826025)"**

## About the Project
Implemented a AIBLOCK framework using **Random Forest Classifier** with **Firestore** as a database. For Serverless Computing database code is hosted on **GCP(Google Cloud Platform)**. Hash Function to create hash value for each block depending on previous block. Hash value ensures data integrity and security of the blockchain. Additionally check blockchain is implemented to detect any changes within the blockchain


## Running the Project
To run the AIBLOCK project, follow these steps:

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/Meesala-Sureshgopi/AIBLOCK-GCP.git
   cd AIBLOCK-GCP
   ```
2. **Install Dependencies:**

  - Make sure Python and Pip are already installed
  
       ```bash
       pip install -r requirements.txt
       ```

3. **Database setup:**
   - Create a firestore database and start a collection by creating an initial block with random hash value.
   - Ensure you have the Firebase credentials (AIBLOCK.json) in your project directory(Configuration).

4. **Training the model:**
   - Initially, we have to train the machine learning model on the *dataset.csv*(kaggle covid dataset) which contains the covid symptoms with values 'yes' or 'no'.
   ``` bash
   python model.py
   ```
   - After training the model it is stored as a file so there's no need to retrain everytime we want a prediction.

5. **Running the Application:**
   
   ```bash
   python prediction.py
   ```
  - Answering the 11 question the model gives prediction on covid
  - This user data is stored in the database inlcuding the symptoms and covid prediction.

6. **Print Blockchain:**
  - This is to view the each block with data and their hash value present in the firestore database.
    
    ```bash
    python print_blockchain.py
    ```
    
    
7. **Check BlockChain:**    

  ```bash
  python check_blockchain.py
  ```
  - It is to check whether a block in the blockchain has been changed or not
