# GitHub Repository Fixes Required

## ⚠️ Status: NOT DEPLOYABLE - 5 Critical Issues Found

Your GitHub repository has the correct code but **critical file organization issues** that prevent deployment on Vercel.

---

## Quick Summary

| Issue | Status | Severity | Fix Time |
|-------|--------|----------|----------|
| Wrong folder structure | ❌ Failed | **CRITICAL** | 5 min |
| Broken vercel.json | ❌ Failed | **CRITICAL** | 2 min |
| Missing api/ folder | ❌ Failed | **CRITICAL** | 2 min |
| Mixed Next.js files | ⚠️ Warning | **HIGH** | 2 min |
| Wrong utils location | ❌ Failed | **CRITICAL** | 2 min |

**Total Fix Time: ~13 minutes**

---

## Issue #1: Wrong Folder Structure

### Problem
All files are in the root directory. Flask expects them in subdirectories.

### What to Do

1. **Create required folders:**
   ```bash
   mkdir -p templates
   mkdir -p static/css
   mkdir -p api
   mkdir -p utils
   ```

2. **Move HTML files to `templates/` folder:**
   ```bash
   git mv index.html templates/
   git mv theory.html templates/
   git mv example1.html templates/
   git mv example2.html templates/
   git mv calculator.html templates/
   ```

3. **Move CSS to `static/css/` folder:**
   ```bash
   git mv style.css static/css/
   ```

4. **Move `jacobi.py` to `utils/` folder:**
   ```bash
   git mv jacobi.py utils/jacobi.py
   ```

5. **Move `index.py` to `api/` folder:**
   ```bash
   git mv index.py api/index.py
   ```

---

## Issue #2: Broken vercel.json

### Problem
The `vercel.json` has an invalid `functions` block that caused your deployment error.

### What to Do

**Replace the entire `vercel.json` with this:**

```json
{
  "buildCommand": "pip install -r requirements.txt",
  "outputDirectory": ".",
  "routes": [
    {
      "src": "^/api/(.*)",
      "dest": "/api/index.py"
    },
    {
      "src": "^/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "^/(.*)",
      "dest": "/api/index.py"
    }
  ]
}
```

Then:
```bash
git add vercel.json
```

---

## Issue #3: Missing api/ Folder

### Problem
`vercel.json` expects `/api/index.py` but there's no api folder.

### What to Do
This is fixed automatically when you complete **Issue #1, Step 5**.

---

## Issue #4: Mixed Next.js Files

### Problem
The repository has leftover files from the old Next.js project that aren't needed.

### What to Do

Delete these files:

```bash
git rm components.json
git rm tsconfig.json
git rm package.json
git rm globals.css
git rm __init__.py
git rm *.tsx  # (if any exist)
```

---

## Issue #5: utils/__init__.py in Wrong Location

### Problem
- Current: `__init__.py` in root (only 55 bytes, empty)
- Needed: `utils/__init__.py` with proper content

### What to Do

1. **Delete the root `__init__.py`:**
   ```bash
   git rm __init__.py
   ```

2. **Create `utils/__init__.py` with proper content:**
   
   Create a new file `utils/__init__.py` with this content:
   ```python
   from .jacobi import JacobiIterationSolver
   
   __all__ = ['JacobiIterationSolver']
   ```

3. **Stage the new file:**
   ```bash
   git add utils/__init__.py
   ```

---

## Complete Step-by-Step Fix Process

### Step 1: Create Folders
```bash
mkdir -p templates
mkdir -p static/css
mkdir -p api
mkdir -p utils
```

### Step 2: Move HTML Files
```bash
git mv index.html templates/
git mv theory.html templates/
git mv example1.html templates/
git mv example2.html templates/
git mv calculator.html templates/
```

### Step 3: Move CSS
```bash
git mv style.css static/css/
```

### Step 4: Move Python Files
```bash
git mv jacobi.py utils/jacobi.py
git mv index.py api/index.py
```

### Step 5: Fix utils/__init__.py
```bash
git rm __init__.py
```

Then create `utils/__init__.py` with:
```python
from .jacobi import JacobiIterationSolver

__all__ = ['JacobiIterationSolver']
```

### Step 6: Fix vercel.json
Replace entire content with the correct config (shown in Issue #2 section)

### Step 7: Delete Unnecessary Files
```bash
git rm components.json
git rm tsconfig.json
git rm package.json
git rm globals.css
```

### Step 8: Commit All Changes
```bash
git add .
git commit -m "Fix folder structure for Flask deployment on Vercel"
git push origin main
```

### Step 9: Deploy
1. Go to Vercel dashboard
2. Click "Redeploy" (or deploy from GitHub)
3. Wait 2-3 minutes
4. Your app should now be live!

---

## Final Project Structure (After Fixes)

```
project/
├── app.py                     ✅ Flask app (no changes needed)
├── vercel.json               ✅ Fixed config
├── requirements.txt          ✅ Dependencies (no changes needed)
├── wsgi.py                   ✅ WSGI wrapper (no changes needed)
│
├── templates/                ← NEW FOLDER
│   ├── index.html
│   ├── theory.html
│   ├── example1.html
│   ├── example2.html
│   └── calculator.html
│
├── static/                   ← NEW FOLDER
│   └── css/
│       └── style.css
│
├── api/                      ← NEW FOLDER
│   └── index.py
│
└── utils/                    ← NEW FOLDER
    ├── __init__.py
    └── jacobi.py
```

---

## Verification Checklist

After applying all fixes, verify:

- [ ] All HTML files are in `templates/` folder
- [ ] CSS file is in `static/css/` folder
- [ ] `jacobi.py` is in `utils/` folder
- [ ] `index.py` is in `api/` folder
- [ ] `utils/__init__.py` exists with proper imports
- [ ] `vercel.json` has correct format (no `functions` block)
- [ ] No `.tsx` or `components.json` files
- [ ] No `tsconfig.json` or `package.json`
- [ ] No `globals.css` (only use `static/css/style.css`)
- [ ] `app.py` is in root directory

---

## Testing Locally (Optional)

After fixes, you can test locally:

```bash
cd /path/to/project
python -m venv venv
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
python app.py
```

Then visit: `http://localhost:5000`

---

## Deployment Readiness After Fixes

Once all fixes are applied:
- ✅ Folder structure: CORRECT
- ✅ vercel.json: VALID
- ✅ API routes: WORKING
- ✅ Deployable: YES

Your app will deploy successfully! 🚀

---

## Questions?

If you have any issues:
1. Check the folder structure matches the diagram above
2. Verify vercel.json matches the format exactly
3. Make sure all files are moved to correct locations
4. Ensure utils/__init__.py has the import statement

After fixes, redeploy and your Jacobi calculator will be live!

