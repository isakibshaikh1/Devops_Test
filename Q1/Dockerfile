# Use the official NGINX image with a specific version for security and stability
FROM nginx:1.19-alpine

# Remove default configuration to avoid conflicts
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf

# Create a non-root user for running NGINX
RUN addgroup -S nginx && adduser -S nginx -G nginx

# Set permissions for NGINX user
RUN chown -R nginx:nginx /var/cache/nginx /var/run /var/log/nginx

# Switch to non-root user
USER nginx

# Expose the HTTP port
EXPOSE 80

# Use the non-root user to run NGINX for better security
CMD ["nginx", "-g", "daemon off;"]
