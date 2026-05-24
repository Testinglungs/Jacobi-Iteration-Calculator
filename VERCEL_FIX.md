# Vercel Deployment Fix Guide

## The Problem

Your serverless function is crashing with error: `500: INTERNAL_SERVER_ERROR` with code `FUNCTION_INVOCATION_FAILED`.

This happens because the Flask app isn't properly configured for Vercel's serverless environment.

## Root Causes & Solutions

I've made the following fixes to your project:

### 1. **Missing Python Package Structure**
- **Problem**: The `utils` folder wasn't recognized as a Python package
- **Fix**: Created `utils/__init__.py` to make it a proper package

### 2. **Incomplete Serverless Handler**
- **Problem**: `api/index.py` wasn't properly exporting the Flask app
- **Fix**: Updated `api/index.py` to properly import and export the WSGI app with error handling

### 3. **Missing Path Configuration**
- **Problem**: Flask couldn't find templates and static files in the serverless environment
- **Fix**: Updated `app.py` to use absolute paths for template and static folders

### 4. **Incorrect Routing Configuration**
- **Problem**: `vercel.json` wasn't properly configured for Flask routing
- **Fix**: Updated `vercel.json` with proper runtime, routes, and function definitions

## Files Changed

1. ✅ **Created**: `utils/__init__.py`
2. ✅ **Updated**: `api/index.py`
3. ✅ **Updated**: `app.py`
4. ✅ **Updated**: `vercel.json`
5. ✅ **Updated**: `.gitignore`

## Next Steps to Deploy

### Step 1: Commit Changes
```bash
git add -A
git commit -m "Fix Vercel deployment configuration"
```

### Step 2: Force Redeploy on Vercel

After pushing to GitHub:
1. Go to your Vercel project dashboard
2. Click "Deployments"
3. Click the three dots on your latest deployment
4. Select "Redeploy" (not "Redeploy with cache")

Or trigger a redeploy by:
- Pushing a new commit to your branch
- Using Vercel CLI: `vercel --prod`

### Step 3: Check Logs

On Vercel dashboard:
1. Go to "Deployments"
2. Click on the latest deployment
3. Go to "Runtime Logs"
4. Look for any import errors or path issues

### Step 4: Test the Deployment

Once deployed, test these URLs:
- `https://your-domain.vercel.app/` - Homepage
- `https://your-domain.vercel.app/theory` - Theory page
- `https://your-domain.vercel.app/calculator` - Calculator
- `https://your-domain.vercel.app/example1` - Example 1

## Common Issues & Solutions

### Issue: "ModuleNotFoundError: No module named 'utils'"
- **Solution**: Make sure `utils/__init__.py` exists
- **Check**: Run `ls -la utils/` and verify `__init__.py` is there

### Issue: "TemplateNotFound"
- **Solution**: Ensure Flask is using absolute paths for template folder
- **Check**: This is fixed in the updated `app.py`

### Issue: "Static files not loading (404)"
- **Solution**: Update static file serving route
- **Check**: This is handled in `vercel.json` routes

### Issue: Still getting "FUNCTION_INVOCATION_FAILED"
- **Solution**: 
  1. Delete `.vercel` folder in your project
  2. Commit and push changes
  3. Trigger a new deployment from scratch

## Verifying Local Deployment

Before pushing to Vercel, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit http://localhost:5000
```

All pages should load correctly with MathJax rendering and the calculator working.

## Still Having Issues?

If the deployment still fails:
1. Check Vercel Runtime Logs for the exact error
2. Ensure all files are committed (especially `templates/` and `static/`)
3. Check that Python version is compatible (3.9+ recommended)
4. Try rebuilding by removing `.vercel` folder and redeploying

## Project Structure

Your final structure should look like:

```
.
├── api/
│   └── index.py           # Vercel serverless handler
├── templates/
│   ├── index.html
│   ├── theory.html
│   ├── example1.html
│   ├── example2.html
│   └── calculator.html
├── static/
│   └── css/
│       └── style.css
├── utils/
│   ├── __init__.py        # Make it a package
│   └── jacobi.py
├── app.py                 # Flask application
├── vercel.json            # Vercel config
├── requirements.txt       # Python dependencies
└── wsgi.py               # WSGI entry point
```

All these files should be committed to Git (except `.venv/` and `__pycache__/`).
