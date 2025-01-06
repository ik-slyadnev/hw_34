FROM python:3.12-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    default-jdk \
    wget \
    gnupg \
    libglib2.0-0 \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libexpat1 \
    libxcb1 \
    libxkbcommon0 \
    libx11-6 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \
    libasound2 \
    libatspi2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tests

COPY requirements.txt .

# Установка Python зависимостей
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Установка Playwright
RUN playwright install chromium

# Установка Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz && \
    tar -zxvf allure-2.25.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.25.0/bin/allure /usr/local/bin/allure && \
    rm allure-2.25.0.tgz

COPY . .

# Изменяем команду запуска для генерации Allure-отчетов
CMD ["pytest", "-v", "--alluredir=allure-results"]
