# Use official Node.js LTS image
FROM node:18-alpine

# Create app directory
WORKDIR Docker-2

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy app source code 
COPY . .

# Expose port 3000
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
