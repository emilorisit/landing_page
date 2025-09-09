# Personal Homepage

A minimalist personal homepage optimized for Domeneshop hosting, featuring a clean, responsive design focused on professional presence and social media connections.

## Project Structure

```
www/                # Root directory for web content
├── index.html     # Main HTML file with profile and social links
└── style.css      # Clean, responsive styling
```

## Features

- Minimalist design using vanilla HTML and CSS
- Professional profile presentation with circular avatar
- Responsive layout optimized for all devices
- Social media links with consistent styling:
  - X ("𝕏")
  - Instagram ("ig")
  - Email ("@")
- Zero external dependencies
- Automatic deployment via SFTP

## Development

This is a static website built with vanilla HTML and CSS, emphasizing:
- Pure CSS for layout and styling
- Consistent Unicode symbols for social media icons
- No external dependencies or frameworks
- Mobile-first responsive design

The site is hosted on Domeneshop and automatically deployed when changes are pushed to the main branch.

### Local Development

To test the website locally:
1. Clone the repository
2. Open `www/index.html` in your web browser
3. Make changes to files in the `www/` directory
4. Commit and push to deploy

## Deployment

The website automatically deploys to Domeneshop via SFTP when changes are pushed to the main branch. The deployment process is optimized to only run when changes are detected in the www/ directory.

### Required Secrets

Configure these secrets in your GitHub repository:
- `DOMENESHOP_SFTP_HOST`: Your Domeneshop SFTP host
- `DOMENESHOP_SFTP_USERNAME`: Your Domeneshop SFTP username
- `DOMENESHOP_SFTP_PASSWORD`: Your Domeneshop SFTP password
- `SSH_FINGERPRINT`: SSH fingerprint for secure connection verification

### Security & Optimization

- Secure SFTP deployment with SSH fingerprint verification
- Git diff filtering for efficient deployments
- Parallel file transfers (4 concurrent)
- Automatic remote directory synchronization
- Secure credentials management via GitHub Actions secrets