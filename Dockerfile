# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy everything to container
COPY . .

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
