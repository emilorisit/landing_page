# Personal Homepage

A lightweight personal homepage optimized for Domeneshop hosting, featuring a clean and responsive design for professional and social media profile presentation.

## Repository Structure

```
www/              # Mirror of the server's /www directory
├── index.html    # Main HTML file
├── style.css     # Global styles
└── static/       # Static assets
    └── css/      # Additional CSS files
```

## Development

This is a static website built with HTML, CSS, and Font Awesome icons. The site is hosted on Domeneshop and automatically deployed via FTP when changes are pushed to the main branch.

## Deployment

This website is automatically deployed to Domeneshop via FTP when changes are pushed to the main branch. The deployment is handled by GitHub Actions.

### Setup Requirements

To enable automatic deployment, you need to set up the following secrets in your GitHub repository:

1. `DOMENESHOP_FTP_USERNAME`: Your Domeneshop FTP username
2. `DOMENESHOP_FTP_PASSWORD`: Your Domeneshop FTP password

To add these secrets securely:
1. Go to your GitHub repository
2. Click on "Settings"
3. Navigate to "Secrets and variables" → "Actions"
4. Click "New repository secret"
5. Add each of the secrets mentioned above

### Security Best Practices

- Never commit sensitive information (passwords, API keys, etc.) to the repository
- Secrets are automatically masked in GitHub Actions logs
- The deployment workflow has limited permissions and runs in isolation
- Only whitelisted file types are included in deployment
- Only one deployment can run at a time to prevent conflicts

The deployment workflow will automatically copy the website files from the `www` directory to the `/www` directory on your Domeneshop hosting.

## Local Development

To test the website locally, simply open `www/index.html` in your web browser.