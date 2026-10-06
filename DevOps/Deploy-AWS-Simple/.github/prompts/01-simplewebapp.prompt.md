# Simple Web App

The Web app should be a ReactJS frontend that integrates with the swapi.info API to display information about Star Wars characters, planets, and starships.

The app should have a clean and responsive UI, with separate pages or sections for characters, planets, and starships. Each section should allow users to browse and search through the available data, and display relevant details in a user-friendly format.

Additionally, the app should handle loading states and errors gracefully, providing feedback to the user when data is being fetched or if an error occurs. It should also be optimized for performance and accessibility, ensuring a smooth and inclusive user experience across different devices and screen sizes.

Finally, the app should include proper routing for navigation between different sections, and maintain a consistent look and feel throughout the application.

The app will be built using ReactJS TypeScript and appropriate folder layout consisting of;
- components
- types/interfaces
- pages
- services

The application will be deployed in the Apache httpd container with the **dist** directory serving as the root for the frontend assets.

Ensure that the necessary configuration is made to the Apache httpd server to serve the **dist** directory correctly as the root for the frontend assets, especially for single page application routing.

Create the Dockerfile to build and deploy the ReactJS application in the Apache httpd container, ensuring that the **dist** directory is correctly served as the root for the frontend assets. Additionally, include any necessary configuration files, such as `.htaccess`, to support single page application routing and other server-side requirements.

Create a docker-compose.yml file to allow local checking of the application.