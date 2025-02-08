FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
	FLASK_APP=app.py \
	FLASK_ENV=production

# Copy the application files
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port Flask runs on
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
