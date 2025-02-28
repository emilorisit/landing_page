# Personal Homepage

A lightweight personal homepage optimized for Domeneshop hosting, featuring a clean and responsive design for professional and social media profile presentation.

## Project Structure

```
www/                # Root directory for web content
├── index.html     # Main HTML file with profile and social links
└── style.css      # Custom styles for the homepage
```

## Features

- Clean, minimalist design using vanilla HTML and CSS
- Professional profile presentation with circular avatar
- Responsive layout that works on all devices
- Integrated social media links (LinkedIn, GitHub, X, Instagram)
- Unicode symbols for social media icons
- Automatic deployment to Domeneshop via SFTP

## Development

This is a static website built with vanilla HTML and CSS. The site uses:
- Pure CSS for layout and styling
- Unicode symbols for social media icons
- No external dependencies or frameworks

The site is hosted on Domeneshop and automatically deployed when changes are pushed to the main branch.

### Local Development

To test the website locally:
1. Clone the repository
2. Open `www/index.html` in your web browser
3. Make changes to files in the `www/` directory
4. Commit and push to deploy changes

## Deployment

The website is automatically deployed to Domeneshop via SFTP when changes are pushed to the main branch. The deployment workflow is optimized to only run when changes are detected in the www/ directory.

### Required Secrets

To enable automatic deployment, set up the following secrets in your GitHub repository:

1. `DOMENESHOP_SFTP_HOST`: Your Domeneshop SFTP host
2. `DOMENESHOP_SFTP_USERNAME`: Your Domeneshop SFTP username
3. `DOMENESHOP_SFTP_PASSWORD`: Your Domeneshop SFTP password
4. `SSH_FINGERPRINT`: SSH fingerprint for secure connection verification

### Security Features

- Secure SFTP deployment with SSH fingerprint verification
- Efficient deployment with git diff filtering
- Parallel file transfers for faster updates
- Automatic cleanup of removed files
- GitHub Actions secrets for credential management

### Deployment Optimization

The deployment workflow includes several optimizations:
- Git diff filtering to only deploy when changes are detected in www/
- Parallel file transfers (4 concurrent transfers)
- Single mirror command that handles both uploads and deletions
- Automatic verification of SSH host fingerprints

The deployment workflow ensures that the remote `/www` directory exactly mirrors your local `www/` directory, maintaining a clean and efficient deployment process.