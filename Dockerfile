FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    binwalk \
    yara \
    capstone-tool \
    file \
    curl \
    git \
    gcc \
    make \
    qemu-system \
    flashrom \
    python3-pip \
    retdec \
    afl++ \
    frida-tools \
    ghidra \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install mcp-server flask requests angr manticore pyocd frida-tools unicorn capstone

EXPOSE 8443
CMD ["python", "server.py"]
