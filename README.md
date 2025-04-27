# Simple-CRUD-App-Using-AWS
Simple CRUD App Using AWS

![Screenshot 2025-04-27 111031](https://github.com/user-attachments/assets/8a8b876c-9b16-44d5-9098-86251c1c3d61)

# API Gateway CRUD Operations with CORS

This project demonstrates a simple CRUD (Create, Read, Update, Delete) application using AWS API Gateway, AWS Lambda, and Amazon DynamoDB. The application provides a web interface to perform CRUD operations on appliance data (e.g., name and status) stored in a DynamoDB table, with Cross-Origin Resource Sharing (CORS) enabled for browser compatibility.

## Project Overview

The application allows users to interact with a backend API to manage appliance data. It includes:
- A static HTML page (`index.html`) with JavaScript for frontend interaction.
- Four AWS Lambda functions (`GET.py`, `POST.py`, `PUT.py`, `DELETE.py`) handling CRUD operations.
- A DynamoDB table (`appliance`) to store the data.
- API Gateway endpoints to route HTTP requests to the Lambda functions.

The project showcases how to integrate AWS services to build a scalable and secure CRUD application with CORS support.

## Features

- **Create (POST)**: Add a new appliance with a name and status.
- **Read (GET)**: Retrieve an appliance's details by name.
- **Update (PUT)**: Modify the status of an existing appliance.
- **Delete (DELETE)**: Remove an appliance by name.
- **CORS Support**: Allows cross-origin requests from any domain, enhancing accessibility.
- **Error Handling**: Includes validation and exception handling for robust operation.

## Technologies Used

- **Frontend**:
  - HTML5 for structure.
  - JavaScript for client-side logic and API calls.
- **Backend**:
  - AWS Lambda for serverless function execution.
  - Amazon DynamoDB for NoSQL data storage.
  - AWS API Gateway for RESTful API management.
- **Tools**:
  - AWS SDK for Python (`boto3`) to interact with DynamoDB.
  - CORS headers for cross-origin resource sharing.

## Project Structure

```
API_Gateway_CRUD_Operations/
├── index.html          # Frontend interface for CRUD operations
├── GET.py             # Lambda function for GET requests
├── POST.py            # Lambda function for POST requests
├── PUT.py             # Lambda function for PUT requests
├── DELETE.py          # Lambda function for DELETE requests
├── README.md          # Project documentation
```

## Setup Instructions

### Prerequisites

- An AWS account with appropriate permissions.
- AWS CLI configured with credentials.
- Node.js and npm (for local testing, optional).
- Basic knowledge of AWS services (Lambda, API Gateway, DynamoDB).

### Deployment Steps

1. **Create a DynamoDB Table**:
   - Go to the AWS Management Console.
   - Navigate to DynamoDB and create a table named `appliance`.
   - Set `AppName` as the partition key (String type).

2. **Upload Lambda Functions**:
   - Create a new Lambda function for each Python file (`GET.py`, `POST.py`, `PUT.py`, `DELETE.py`).
   - Use the Python 3.9 runtime (or compatible version).
   - Upload the respective `.py` file as the function code.
   - Ensure the Lambda role has permissions for DynamoDB access (e.g., `AmazonDynamoDBFullAccess`).

3. **Set Up API Gateway**:
   - Create a new REST API in API Gateway.
   - Define resources and methods:
     - `/GET/{AppName}` with GET method (mapped to `GET.py`).
     - `/POST` with POST method (mapped to `POST.py`).
     - `/PUT` with PUT method (mapped to `PUT.py`).
     - `/DELETE/{AppName}` with DELETE method (mapped to `DELETE.py`).
   - Enable CORS for each method:
     - Add `Access-Control-Allow-Origin: *`.
     - Include `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers`.
   - Deploy the API to a stage (e.g., `PROD`) and note the invoke URL (e.g., `https://i1qrnm2fgb.execute-api.us-east-1.amazonaws.com/PROD`).

4. **Update `index.html`**:
   - Replace the `fetch` URLs in the JavaScript with your deployed API Gateway URL.

5. **Test the Application**:
   - Open `index.html` in a browser.
   - Use the form fields to perform CRUD operations and view results in the output section.

### Local Testing (Optional)

- Serve `index.html` locally using a simple HTTP server:
  ```bash
  npx http-server
  ```
- Ensure the API Gateway URL points to your deployed endpoint.

## Usage

1. **GET Data**:
   - Enter an appliance name (e.g., `Light`) and click "Fetch Data".
   - View the retrieved item or an error if not found.

2. **POST Data**:
   - Enter a name and status (e.g., `Fan`, `On`) and click "Post Data".
   - Receive a success message or an error if the item exists.

3. **PUT Data**:
   - Enter a name and new status (e.g., `Fan`, `Off`) and click "Update Data".
   - Receive a success message or an error if the item isn’t found.

4. **DELETE Data**:
   - Enter an appliance name (e.g., `Fan`) and click "Delete Data".
   - Receive a success message or an error if the item isn’t found.

## Screenshots
![Screenshot 2025-04-27 111031](https://github.com/user-attachments/assets/43317597-9435-418f-9c43-a9660070283b)

- **Network Requests**:  Shows successful DELETE request with CORS headers.
- **Interface**: The HTML page with input fields and output display.
<img width="960" alt="Page and dev tool to inspect" src="https://github.com/user-attachments/assets/a9c29d65-8913-4466-8733-a6123f9b7a1d" />
<img width="212" alt="Delete and get api creation formate" src="https://github.com/user-attachments/assets/da4dfda2-cd4e-40be-ac21-5ec3a7886fdc" />
<img width="212" alt="get,post,put creation formate" src="https://github.com/user-attachments/assets/a7a41d7c-9ecd-4fb4-8fea-7504e1ede29e" />

## Potential Improvements

- **Authentication**: Add API key or IAM authentication to secure endpoints.
- **Validation**: Enhance input validation (e.g., regex for names).
- **Error Logging**: Implement structured logging for Lambda functions.
- **Frontend Styling**: Use CSS frameworks (e.g., Bootstrap) for a better UI.
- **Batch Operations**: Support bulk CRUD operations via API Gateway.



## Acknowledgments

- Inspired by AWS documentation and community examples.
- Thanks to the AWS team for providing robust serverless tools.

## Contributing

Feel free to fork this repository, submit issues, or send pull requests. Contributions are welcome!

---

## Follow Along Files

Follow along files and A comphrensive Guide ( Cook Book ) is Attached in the files you can have  a look.
