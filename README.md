## Multi-Stage Docker Build – Node.js Application

This project demonstrates the use of multi-stage Docker builds to create
a lightweight and production-ready Docker image for a Node.js application.

### Key Features
- Multi-stage Dockerfile
- Reduced image size
- Clean separation of build and runtime stages
- Production-ready container

### Technologies Used
- Docker
- Node.js
- Express

### How to Run
docker build -t multistage-node-app .
docker run -p 3000:3000 multistage-node-app

## multistage-docker-node-app/
│
├── app/
│   ├── server.js
│   └── package.json
│
├── Dockerfile
├── .dockerignore
└── README.md

## Dockerfile Explanation

Stage 1 (Builder Stage)
Installs dependencies and prepares the application.

Stage 2 (Production Stage)
Copies only the required files from the builder stage and runs the application.

This ensures the final image does not contain unnecessary build tools.

## Access the Application

Open your browser and visit:

http://localhost:3000

## Benefits of Multi-Stage Docker Builds

✅ Smaller Docker image size

✅ Faster container startup time

✅ Clean and optimized production environment

✅ Industry-standard Docker practice

## Learning Outcome

-Through this project, I learned:

-How multi-stage Docker builds work

-How to optimize Docker images

-How to separate build and runtime environments

-How Docker is used in real-world production setups
