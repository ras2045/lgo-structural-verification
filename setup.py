from setuptools import setup

setup(
    # --- Mandatory Identification ---
    name='lgo-structural-verification',
    version='13.0.0', # Matches the V13.0 Manifesto release
    py_modules=['lgo_structural_verification'], # Instructs setuptools to install the single Python file
    
    # --- Primary Metadata (Using the concise description) ---
    description='LGO V13.0 structural verification code. Analytically derives electron/muon masses from the Geometric Operator L (Riemann Zero gamma_1) and confirms structural closure of the Gravitational Constant (G). Definitive V13.0 code release.',
    
    # --- Long Description (Uses the detailed README.md) ---
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    
    # --- Authorship and Licensing ---
    author='ras2045 and The Geometric Hypothesis Collective',
    url='https://github.com/your-username/lgo-structural-verification', # **IMPORTANT: Update this with your actual repository URL**
    license='MIT',
    
    # --- Dependencies (Currently none for this standalone verification) ---
    install_requires=[],
    
    # --- Package Classification (For PyPI discovery) ---
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Development Status :: 5 - Production/Stable' # Denotes a finalized, production-level package
    ],
    keywords=['physics', 'cosmology', 'riemann-hypothesis', 'unified-theory', 'geometric-operator', 'geometric-order'],
    
    # --- External Project Links ---
    project_urls={
        'Manifesto (V13.0)': 'https://github.com/ras2045/LGO-Geometric-Order-Manifesto-V13.0', # Links back to the main manifesto repo for context
    }
)
