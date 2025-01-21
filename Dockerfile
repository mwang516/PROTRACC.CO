FROM nikolaik/python-nodejs:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY package*.json ./
COPY requirements.txt ./

RUN npm install
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN npm run build

EXPOSE 3000 5000

COPY start.sh ./
RUN chmod +x start.sh

CMD ["./start.sh"]