# Use a base image with Python and common tools pre-installed
FROM gitpod/workspace-full:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PATH /workspace/.venv/bin:$PATH

# Install system dependencies
RUN sudo apt-get update && sudo apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    libgl1-mesa-glx \
    && sudo apt-get clean

# Create and activate a virtual environment
RUN python3 -m venv /workspace/.venv

# Copy project requirements
COPY requirements.txt /workspace/

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r /workspace/requirements.txt

# Install additional tools (optional, for development purposes)
RUN npm install -g prettier

# Set up the working directory
WORKDIR /workspace/

# Expose necessary ports
EXPOSE 8000 5000

# Commands to run after container starts
CMD ["bash"]
