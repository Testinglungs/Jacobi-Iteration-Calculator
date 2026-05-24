"""
Jacobi Iteration Algorithm Implementation
Solves systems of linear equations Ax = b using the Jacobi iterative method
"""

from typing import Dict, List, Tuple, Any
import math


class JacobiIterationSolver:
    """
    Solves a system of linear equations using the Jacobi iteration method.
    For a system Ax = b, rearranges to solve each equation for one variable.
    """
    
    def __init__(self, matrix: List[List[float]], vector: List[float], 
                 tolerance: float = 1e-6, max_iterations: int = 100):
        """
        Initialize the Jacobi solver.
        
        Args:
            matrix: Coefficient matrix A (n x n)
            vector: Constants vector b (n x 1)
            tolerance: Convergence tolerance
            max_iterations: Maximum number of iterations
        """
        self.A = [row[:] for row in matrix]  # Copy matrix
        self.b = vector[:]  # Copy vector
        self.n = len(matrix)
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        
    def is_diagonally_dominant(self) -> bool:
        """Check if matrix is diagonally dominant (sufficient for convergence)."""
        for i in range(self.n):
            diagonal = abs(self.A[i][i])
            sum_rest = sum(abs(self.A[i][j]) for j in range(self.n) if i != j)
            if diagonal <= sum_rest:
                return False
        return True
    
    def solve(self) -> Dict[str, Any]:
        """
        Solve the system using Jacobi iteration.
        
        Returns:
            Dictionary containing:
            - solution: final approximate solution
            - iterations: number of iterations performed
            - converged: whether solution converged
            - steps: detailed step-by-step iteration data
            - diagonal_dominant: whether matrix is diagonally dominant
            - residuals: residual error at each iteration
        """
        # Check diagonal dominance
        diag_dominant = self.is_diagonally_dominant()
        
        # Initialize solution vectors
        x_old = [0.0] * self.n
        x_new = [0.0] * self.n
        
        steps = []
        residuals = []
        
        for iteration in range(self.max_iterations):
            # Perform Jacobi iteration
            for i in range(self.n):
                sum_val = 0.0
                for j in range(self.n):
                    if i != j:
                        sum_val += self.A[i][j] * x_old[j]
                
                x_new[i] = (self.b[i] - sum_val) / self.A[i][i]
            
            # Calculate residual (maximum absolute difference)
            residual = max(abs(x_new[i] - x_old[i]) for i in range(self.n))
            residuals.append(residual)
            
            # Store step information
            steps.append({
                'iteration': iteration + 1,
                'solution': x_new[:],
                'residual': residual,
                'old_solution': x_old[:]
            })
            
            # Check convergence
            if residual < self.tolerance:
                return {
                    'solution': x_new,
                    'iterations': iteration + 1,
                    'converged': True,
                    'steps': steps,
                    'diagonal_dominant': diag_dominant,
                    'residuals': residuals,
                    'final_residual': residual
                }
            
            # Update for next iteration
            x_old = x_new[:]
        
        # Max iterations reached
        return {
            'solution': x_new,
            'iterations': self.max_iterations,
            'converged': False,
            'steps': steps,
            'diagonal_dominant': diag_dominant,
            'residuals': residuals,
            'final_residual': residuals[-1] if residuals else float('inf')
        }
    
    def get_iteration_details(self, step_index: int) -> Dict[str, Any]:
        """Get detailed calculation info for a specific iteration."""
        if step_index < 0 or step_index >= len(self.steps):
            return {}
        
        return self.steps[step_index]


def format_iteration_for_display(step: Dict[str, Any], matrix: List[List[float]], 
                                  vector: List[float]) -> str:
    """
    Format a single iteration step for HTML display with mathematical notation.
    
    Args:
        step: Dictionary containing iteration data
        matrix: Original coefficient matrix
        vector: Original constant vector
        
    Returns:
        HTML string with formatted iteration step
    """
    iteration_num = step['iteration']
    x_old = step['old_solution']
    x_new = step['solution']
    residual = step['residual']
    n = len(matrix)
    
    html = f"<h4>Iteration {iteration_num}</h4>\n"
    html += "<p><strong>Previous approximation:</strong> "
    html += "$$x^{(" + str(iteration_num - 1) + ")} = ["
    html += ", ".join([f"{x:.6f}" for x in x_old])
    html += "]^T$$</p>\n"
    
    html += "<p><strong>Calculations:</strong></p>\n"
    html += "<ul>\n"
    
    for i in range(n):
        html += f"<li>$$x_{{ {i+1} }}^{{ ({iteration_num}) }} = "
        html += f"\\frac{{ {vector[i]:.4f}"
        
        # Add sum of other terms
        sum_parts = []
        for j in range(n):
            if i != j:
                coeff = matrix[i][j]
                x_val = x_old[j]
                if coeff >= 0:
                    sum_parts.append(f"+ {coeff:.4f} \\times {x_val:.6f}")
                else:
                    sum_parts.append(f"- {abs(coeff):.4f} \\times {x_val:.6f}")
        
        if sum_parts:
            html += " " + " ".join(sum_parts)
        
        html += f"}} {{ {matrix[i][i]:.4f} }} = {x_new[i]:.6f}$$</li>\n"
    
    html += "</ul>\n"
    html += f"<p><strong>Maximum change (residual):</strong> $$||x^{{ ({iteration_num}) }} - x^{{ ({iteration_num-1}) }}||_\\infty = {residual:.2e}$$</p>\n"
    
    return html
