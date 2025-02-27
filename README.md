# Personal Homepage

A minimalist personal homepage showcasing professional and social media profiles with a clean, lightweight design.

## Deployment

This website is automatically deployed to Domeneshop via SFTP when changes are pushed to the main branch. The deployment is handled by GitHub Actions.

### Setup Requirements

To enable automatic deployment, you need to set up the following secrets in your GitHub repository:

1. `DOMENESHOP_SFTP_HOST`: Your Domeneshop SFTP server hostname
2. `DOMENESHOP_SFTP_USERNAME`: Your Domeneshop SFTP username
3. `DOMENESHOP_SFTP_PASSWORD`: Your Domeneshop SFTP password

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
- Sensitive files and directories are excluded from deployment
- Only one deployment can run at a time to prevent conflicts

The deployment workflow will automatically copy the website files to the `/www` directory on your Domeneshop hosting.

## Development

To run the website locally:

```bash
python main.py
```

The website will be available at `http://localhost:5000`.