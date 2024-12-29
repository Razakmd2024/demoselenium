ARG PORT=5000
FROM cypress/browsers:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python-is-python3 python3-pip python3-venv unzip wget

# Install Chrome dependencies
RUN apt-get install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libx11-xcb1 libxcomposite1 libxcursor1 libxi6 libxrandr2 libasound2 libpangocairo-1.0-0 libatk1.0-0 libcups2 libxdamage1 libxss1 libxtst6 fonts-liberation libappindicator3-1 xdg-utils

# Create and activate a virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:${PATH}"

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000", "--timeout", "120"]

