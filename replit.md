# replit.md

## Overview

This is a minimalist personal homepage project built with vanilla HTML and CSS. The site serves as a professional digital presence, featuring a clean profile layout with social media links. It's designed to be hosted on Domeneshop with automatic SFTP deployment and emphasizes simplicity with zero external dependencies.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Pure Static Site**: Built with vanilla HTML and CSS without any frameworks or build tools
- **Single Page Application**: Contains only one HTML file (`index.html`) with accompanying stylesheet
- **Mobile-First Design**: Responsive layout using CSS flexbox for centering and alignment
- **Zero Dependencies**: No external libraries, frameworks, or CDN resources

### Styling Approach
- **System Fonts**: Uses native font stack for optimal performance and consistency
- **Unicode Icons**: Social media links use Unicode symbols instead of icon fonts or images
- **CSS Reset**: Custom reset for consistent cross-browser rendering
- **Flexbox Layout**: Modern CSS layout for responsive design

### Content Strategy
- **External Profile Image**: Uses LinkedIn CDN for profile picture (avoids local file management)
- **Direct Social Links**: Each social platform links directly to external profiles
- **Email Integration**: Uses contact email service for communication

## External Dependencies

### Hosting and Deployment
- **Domeneshop Hosting**: Static file hosting service
- **SFTP Deployment**: Automated deployment pipeline (triggered by repository changes)

### Third-Party Services
- **LinkedIn CDN**: Profile image hosting and delivery
- **Social Media Platforms**: Direct links to LinkedIn, GitHub, X (Twitter), Instagram
- **Email Service**: contact.scheming298@passinbox.com for contact functionality

### Development Tools
- **Git Version Control**: Repository management and deployment triggers
- **Web Browser**: Local development and testing environment