FROM python:3.11-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /andrii_mazur
COPY src /andrii_mazur/src

EXPOSE 8501
CMD ["python", "src/main.py"]
# CMD ["streamlit", "run", "src/window_strimlit.py", "--server.port=8501", "--server.address=0.0.0.0"]