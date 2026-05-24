# Jacobi Iteration Numerical Methods Calculator

A comprehensive Flask web application for understanding and solving systems of linear equations using the Jacobi iteration method. This educational tool provides mathematical theory, worked examples, and an interactive calculator for numerical methods learning.

## Features

### 📚 Mathematical Content
- **Theory Page**: Comprehensive mathematical background on Jacobi iteration including:
  - Problem formulation
  - Iteration formula derivation
  - Convergence conditions (diagonal dominance)
  - Stopping criteria
  - Comparison with other methods

### 💡 Worked Examples
- **Example 1**: Detailed solution of a 3×3 linear system with step-by-step iterations
- **Example 2**: Complete solution of a 4×4 linear system with all intermediate calculations
- All examples include convergence verification and final solution validation

### 🧮 Interactive Calculator
- **Dynamic Matrix Input**: Solve systems of size n×n (2 to 8 dimensions)
- **Real-time Computation**: Uses the Jacobi iteration algorithm
- **Detailed Results Display**:
  - Solution vector in mathematical notation
  - Convergence status and number of iterations
  - Diagonal dominance checking
  - Iteration-by-iteration residuals
  - Optional detailed step display for first 10 iterations
- **Load Example Problems**: Quick-load pre-defined example systems

## Technologies

- **Backend**: Flask 2.3.0 (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **Mathematics**: MathJax 3 for LaTeX equation rendering
- **Algorithm**: Manual implementation of Jacobi iteration method

## Project Structure

```
jacobi-calculator/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment configuration
├── wsgi.py                  # WSGI entry point
├── api/
│   └── index.py            # Serverless function handler
├── templates/
│   ├── index.html          # Landing page
│   ├── theory.html         # Mathematical theory
│   ├── example1.html       # 3×3 system worked example
│   ├── example2.html       # 4×4 system worked example
│   └── calculator.html     # Interactive calculator
├── static/
│   └── css/
│       └── style.css       # Application styling
└── utils/
    └── jacobi.py          # Jacobi algorithm implementation
```

## Installation

### Local Development

1. Clone or download the project
2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask development server:
   ```bash
   python app.py
   ```

5. Open your browser to `http://localhost:5000`

## Deployment to Vercel

### Prerequisites
- Vercel account (free at https://vercel.com)
- GitHub repository with the project code

### Steps

1. **Create a GitHub Repository**
   - Push your code to GitHub

2. **Deploy to Vercel**
   - Go to https://vercel.com and sign in with GitHub
   - Click "New Project"
   - Select your repository
   - Vercel will automatically detect Flask and configure the build

3. **Configuration**
   - The `vercel.json` file contains the necessary configuration
   - Vercel will install dependencies from `requirements.txt`
   - The app will be served at `https://your-project.vercel.app`

## API Endpoints

### GET / (and other pages)
Returns the HTML pages for navigation

### POST /api/solve
Solves a system using Jacobi iteration

**Request Body**:
```json
{
  "matrix": [[10, 1, 1], [1, 10, 1], [1, 1, 10]],
  "vector": [12, 12, 12],
  "tolerance": 1e-6,
  "max_iterations": 100
}
```

**Response**:
```json
{
  "solution": [1.0, 1.0, 1.0],
  "iterations": 10,
  "converged": true,
  "diagonal_dominant": true,
  "final_residual": 6.144e-07,
  "residuals": [...],
  "steps": [
    {
      "iteration": 1,
      "solution": [...],
      "residual": 1.2
    },
    ...
  ]
}
```

## Algorithm Details

The Jacobi iteration method solves a system Ax = b by iteratively refining the solution:

$$x_i^{(k+1)} = \frac{1}{a_{ii}} \left( b_i - \sum_{j \neq i} a_{ij} x_j^{(k)} \right)$$

### Convergence Conditions
- **Diagonal Dominance**: The matrix must be diagonally dominant for guaranteed convergence
  $$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \text{ for all } i$$

### Stopping Criteria
The iteration stops when:
- Residual: $$||x^{(k)} - x^{(k-1)}||_\infty < \epsilon$$
- Maximum iterations reached

## Educational Use

This calculator is designed for:
- Understanding iterative methods for solving linear systems
- Learning numerical analysis concepts
- Comparing convergence behavior across different matrix properties
- Studying the importance of diagonal dominance in numerical methods

## Browser Support

Works on all modern browsers that support:
- ES6 JavaScript
- CSS Grid and Flexbox
- Fetch API
- MathJax 3

## License

Educational tool created for PIT Numerical Methods course.

## Authors

Created as part of the Numerical Methods online calculator project series.

---

**Version**: 1.0  
**Last Updated**: May 2026
