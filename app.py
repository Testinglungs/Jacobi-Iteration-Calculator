"""
Flask application for Jacobi Iteration Numerical Methods Calculator
"""

from flask import Flask, render_template, jsonify, request
from utils.jacobi import JacobiIterationSolver
import json
import os

# Get the absolute path for templates and static folders
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)


@app.route('/')
def index():
    """Landing page with navigation."""
    return render_template('index.html')


@app.route('/theory')
def theory():
    """Theory and mathematical background page."""
    return render_template('theory.html')


@app.route('/example1')
def example1():
    """First worked example (3x3 system)."""
    return render_template('example1.html')


@app.route('/example2')
def example2():
    """Second worked example (4x4 system)."""
    return render_template('example2.html')


@app.route('/calculator')
def calculator():
    """Interactive calculator page."""
    return render_template('calculator.html')


@app.route('/api/solve', methods=['POST'])
def solve():
    """
    API endpoint for solving a system using Jacobi iteration.
    
    Expected JSON input:
    {
        "matrix": [[a11, a12, ...], [a21, a22, ...], ...],
        "vector": [b1, b2, ...],
        "tolerance": 1e-6,
        "max_iterations": 100
    }
    """
    try:
        data = request.get_json()
        
        # Validate input
        if not data or 'matrix' not in data or 'vector' not in data:
            return jsonify({'error': 'Missing matrix or vector'}), 400
        
        matrix = data['matrix']
        vector = data['vector']
        
        # Validate dimensions
        if not matrix or not vector:
            return jsonify({'error': 'Empty matrix or vector'}), 400
        
        if len(matrix) != len(vector):
            return jsonify({'error': 'Matrix and vector dimensions do not match'}), 400
        
        if any(len(row) != len(matrix) for row in matrix):
            return jsonify({'error': 'Matrix must be square'}), 400
        
        # Check for zero diagonal elements
        for i in range(len(matrix)):
            if matrix[i][i] == 0:
                return jsonify({'error': f'Zero diagonal element at position ({i+1},{i+1})'}), 400
        
        # Get parameters
        tolerance = float(data.get('tolerance', 1e-6))
        max_iterations = int(data.get('max_iterations', 100))
        
        # Solve using Jacobi iteration
        solver = JacobiIterationSolver(matrix, vector, tolerance, max_iterations)
        result = solver.solve()
        
        # Format response
        return jsonify({
            'solution': result['solution'],
            'iterations': result['iterations'],
            'converged': result['converged'],
            'diagonal_dominant': result['diagonal_dominant'],
            'final_residual': result['final_residual'],
            'residuals': result['residuals'],
            'steps': [
                {
                    'iteration': step['iteration'],
                    'solution': step['solution'],
                    'residual': step['residual']
                }
                for step in result['steps']
            ]
        })
    
    except ValueError as e:
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Calculation error: {str(e)}'}), 500


@app.route('/api/check-convergence', methods=['POST'])
def check_convergence():
    """Check if matrix is diagonally dominant."""
    try:
        data = request.get_json()
        matrix = data.get('matrix', [])
        
        if not matrix or any(len(row) != len(matrix) for row in matrix):
            return jsonify({'error': 'Invalid matrix'}), 400
        
        solver = JacobiIterationSolver(matrix, [0] * len(matrix))
        is_dominant = solver.is_diagonally_dominant()
        
        return jsonify({
            'diagonally_dominant': is_dominant,
            'message': 'Matrix is diagonally dominant (convergence likely)' if is_dominant 
                      else 'Matrix is NOT diagonally dominant (convergence not guaranteed)'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Page not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
