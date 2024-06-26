# Face Comparison API - ReadMe

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Error Handling](#error-handling)
- [License](#license)

## Requirements

- Python 3.7+
- Flask
- requests
- DeepFace

## Installation

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Make sure to include a `requirements.txt` file with the necessary dependencies:

   ```
   Flask==2.1.2
   requests==2.27.1
   deepface==0.0.75
   ```

3. **Run the Application:**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://0.0.0.0:105`.

## Usage

### Sample Request

To verify if two images are of the same person, you can use a tool like `curl` or Postman to send a POST request.

**Example with `curl`:**

```bash
curl -X POST http://0.0.0.0:105/verify/ \
    -F "img1=@/path/to/local/image.jpg" \
    -F "img2=http://example.com/image2.jpg"
```

### Expected Response

A successful response will be in JSON format, indicating whether the images are of the same person and including additional details about the comparison.

**Example Response:**

```json
{
  "data": {
    "verified": true,
    "distance": 0.3,
    "max_threshold_to_verify": 0.4,
    "model": "VGG-Face",
    "similarity_metric": "cosine"
  },
  "success": true
}
```

## Endpoints

### `/verify/` - POST

- **Description:** Verifies if two images are of the same person.
- **Parameters:**
  - `img1` (file): The first image file.
  - `img2` (string): The URL of the second image.
- **Response:**
  - `200 OK`: If the comparison is successful.
  - `400 Bad Request`: If the URL is invalid.
  - `500 Internal Server Error`: If any other error occurs.

**Example Request:**

```http
POST /verify/
Content-Type: multipart/form-data

img1: (file)
img2: http://example.com/image2.jpg
```

### `/test` - GET

- **Description:** Simple test endpoint to check if the server is running.
- **Response:**
  - `200 OK`: If the server is running correctly.
  - `500 Internal Server Error`: If any error occurs.

**Example Request:**

```http
GET /test
```

**Example Response:**

```json
{
  "data": "Success",
  "success": true
}
```

## Error Handling

The API handles errors gracefully and provides meaningful messages to the client. Errors include:

- Invalid image URL.
- Internal server errors during processing.

**Example Error Response:**

```json
{
  "error": "Invalid image URL",
  "success": false
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or raise issues for enhancements and bug fixes!
