# Use the official Python image as the base image  
FROM python:3.8
  
# Set the working directory  
WORKDIR /app  
  
# Copy the requirements.txt file into the container  
COPY requirements.txt .  

COPY . .
  
# Install the dependencies  
RUN pip install --no-cache-dir -r requirements.txt  

#RUN sleep 460
  
# Copy the rest of the application code into the container  
COPY . .  

# Expose the port the app will run on  
EXPOSE 8000  
  
# Run the Flask application as root  
CMD ["python", "main.py"]  
