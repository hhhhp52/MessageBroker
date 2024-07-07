# MessageBroker

## How To Run It

### Using Make Command

1. **Run locally:**
   1. Open your terminal.
   2. Clone the repository:
      ```
      git clone git@github.com:hhhhp52/MessageBroker.git
      ```
   3. Navigate to the project directory:
      ```
      cd MessageBroker
      ```
   4. Run RabbitMQ by docker
      ```
      docker run -it --privileged --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
      ```
      or
      ```
      make start-rabbit-mq
      ```
   5. Start the server:
      ```
      python3 server.py
      ```
      or
      ```
      make run-server
      ```

   6. Start the client:
      ```
      python3 client.py
      ```
      or
      ```
      make run-client
      ```

---

## Directory Structure

- **ApiCreation/**
  - `.gitignore`: Ignores files not pushed to GitHub.
  - `Makefile`: Provides convenient commands for execution.
  - `requirements.txt`: Specifies Python package dependencies and versions.
  - `client.py`: Client for sending the message to rabbitMQ.
  - `server.py`: Server for receiving the message from rabbitMQ.

## Example GIF

![Example GIF](./MessageBroker.gif)