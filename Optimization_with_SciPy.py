#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf
from scipy.optimize import minimize_scalar

# Load data
exp_data = np.load("I_q_IPA_exp.npy")
model_data = np.load("I_q_IPA_model.npy")

# Extract q and intensity
q_exp, I_exp = exp_data[:, 0], exp_data[:, 1]
q_model, I_model = model_data[:, 0], model_data[:, 1]

# Interpolate model onto experimental q-values
rbf = Rbf(q_model, I_model)  
I_model_interp = rbf(q_exp)

# Remove invalid points
mask = ~np.isnan(I_model_interp) & ~np.isnan(I_exp)
I_model_interp = I_model_interp[mask]
I_exp = I_exp[mask]
q_exp = q_exp[mask]

# Define error function (least squares)
def error(a):
    return np.sum(np.abs(a * I_model_interp - I_exp))

# Find optimal scaling factor
result = minimize_scalar(error)
a_opt = result.x

print(f"Optimal scaling factor: {a_opt}")

# Compute fitted model
I_fit = a_opt * I_model_interp

# Plot results
plt.figure(figsize=(6,4))
plt.scatter(q_exp, I_exp, label="Experimental", s=10)
plt.plot(q_exp, I_fit, label="Fitted Model", color="red")
plt.xlabel("q")
plt.ylabel("Intensity")
plt.legend()
plt.grid()
plt.title("Model Fit to Experimental Data")
plt.show()