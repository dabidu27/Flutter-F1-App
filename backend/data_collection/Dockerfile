FROM python:3.11-slim

# set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of backend code
COPY . .

#run the app
CMD ["uvicorn", "endpoints:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]