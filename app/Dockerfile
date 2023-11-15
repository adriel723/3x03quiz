FROM python:3.10.12

# Set the working directory in the container
WORKDIR /home/user1

# Create a group and user to run the app
# Note: The -S option does not exist in the addgroup and adduser for Ubuntu, it's used in Alpine
RUN groupadd -r user1 && \
    useradd --no-log-init -r -g user1 user1

# Copy the current directory contents into the container at /home/user1
COPY ./requirements.txt ./requirements.txt
COPY ./app.py ./app.py
COPY ./templates/ ./templates/
#COPY ./list.txt ./list.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8001 available to the world outside this container
EXPOSE 8001

# Change to non-root user
USER user1

# Run app.py when the container launches
CMD ["python", "app.py"]


