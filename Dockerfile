FROM python:3.11-slim
COPY requriments.txt .
RUN pip install --no-cache-dir -r requriments.txt
COPY app.py .
EXPOSE 5002
CMD ["python", "app.py"]
