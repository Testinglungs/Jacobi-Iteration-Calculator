# Deploying the Jacobi Iteration Calculator to Vercel

This guide walks you through deploying your Flask application to Vercel in just a few steps.

## Prerequisites

- A GitHub account (free at https://github.com)
- A Vercel account (free at https://vercel.com)
- Git installed on your computer

## Step 1: Prepare Your Code for GitHub

### Option A: Using the v0 Download

1. Download the project as a ZIP file from v0
2. Create a new folder on your computer
3. Extract the ZIP file into that folder
4. Open a terminal/command prompt in that folder

### Option B: Clone from Existing Repository

If you already have a GitHub repository, ensure all the project files are there.

## Step 2: Initialize Git and Push to GitHub

### If you don't have a GitHub repository yet:

1. Go to https://github.com/new and create a new repository
   - Name it something like "jacobi-iteration-calculator"
   - Choose "Public" or "Private" based on your preference
   - Do NOT initialize with README (we already have one)

2. In your terminal, run these commands:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Jacobi Iteration Calculator"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/jacobi-iteration-calculator.git
   git push -u origin main
   ```
   Replace `YOUR_USERNAME` with your GitHub username.

### If you already have a repository:

```bash
git add .
git commit -m "Add Jacobi iteration calculator"
git push
```

## Step 3: Deploy to Vercel

1. Go to https://vercel.com/new
2. Click "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Select your "jacobi-iteration-calculator" repository
5. Click "Import"

## Step 4: Configure Vercel (Optional)

Vercel should automatically detect this as a Flask application. The configuration is already in `vercel.json`. You can leave all settings as default and click "Deploy".

## Step 5: Wait for Deployment

Vercel will:
1. Install Python dependencies from `requirements.txt`
2. Build your application
3. Deploy it to Vercel's global network

You'll see a URL like: `https://jacobi-iteration-calculator.vercel.app`

## Step 6: Test Your Deployment

1. Click the URL provided by Vercel
2. Test all pages:
   - Home page
   - Theory page
   - Example 1 and Example 2
   - Interactive Calculator (try solving a system)

## Troubleshooting

### Build Fails
- Check that `requirements.txt` exists and has the correct Python packages
- Ensure `app.py` is in the root directory
- Check that all templates are in the `templates/` directory

### Pages Not Loading
- Verify all HTML files are in the `templates/` folder
- Check that `static/css/style.css` exists
- Ensure the file paths in `vercel.json` are correct

### Calculator Not Working
- Check the Vercel logs for Python errors
- Verify the `utils/jacobi.py` file exists and is correctly formatted
- Test the API locally first before redeploying

## Making Updates

After deployment, if you make changes:

1. Update your code locally
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. Vercel will automatically redeploy within seconds

## View Deployment Logs

Go to your Vercel dashboard (https://vercel.com/dashboard) to:
- View deployment status
- Check build and runtime logs
- Manage environment variables
- Configure custom domains

## Production Tips

1. **Performance**: The application uses MathJax from a CDN - it's cached after first load
2. **Scaling**: Vercel automatically scales to handle traffic
3. **Cost**: Jacobi Calculator stays within Vercel's free tier limits
4. **Monitoring**: Use Vercel Analytics to monitor performance

## Custom Domain (Optional)

To use your own domain:

1. In Vercel Dashboard, go to your project
2. Click "Settings" → "Domains"
3. Add your custom domain
4. Follow the DNS instructions from your domain provider

## Support

If you encounter any issues:
- Check Vercel's documentation: https://vercel.com/docs
- Review the application logs in Vercel Dashboard
- Ensure all Python dependencies are installed locally first

---

Your Jacobi Iteration Calculator is now ready for the world to use!
