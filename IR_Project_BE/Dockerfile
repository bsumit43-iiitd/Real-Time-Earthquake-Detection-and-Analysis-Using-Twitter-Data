# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

RUN pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache --trusted-host pypi.python.org -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 5000

# Run the Django development server when the container launches
CMD ["python", "app.py"]
