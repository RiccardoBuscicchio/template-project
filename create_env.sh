#!/bin/bash

# Help message
function show_help {
    echo "Usage: ./create_env.sh <env_name> [packages.yml]"
    echo ""
    echo "Create a new Conda environment, activate it, install ipykernel, and register the kernel with Jupyter Lab."
    echo ""
    echo "Arguments:"
    echo "  <env_name>     Name of the Conda environment to create"
    echo "  [packages.yml] Optional YAML file with a list of packages to install"
    echo ""
    echo "Options:"
    echo "  -h, --help     Show this help message and exit"
}

# Check if the help option is provided
if [[ $1 == "-h" || $1 == "--help" ]]; then
    show_help
    exit 0
fi

# Check if the environment name is provided
if [ -z "$1" ]; then
    echo "Please provide a name for the Conda environment."
    show_help
    exit 1
fi

# Assign the provided environment name
env_name="$1"

# Create a new Conda environment
conda create -y -n $env_name

# Activate the Conda environment
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate $env_name

# Install additional packages if a YAML file is provided
if [ ! -z "$2" ]; then
    packages_file="$2"
    echo "Installing additional packages from $packages_file"
    conda install -y --file "$packages_file"
fi

# Install ipykernel
conda install -y ipykernel

# Register the kernel with Jupyter Lab
python -m ipykernel install --user --name $env_name --display-name "$env_name"

# Deactivate the Conda environment
conda deactivate

# Helper documentation
echo "Conda environment '$env_name' created successfully."
echo "To activate the environment, run:"
echo "    conda activate $env_name"
echo ""
echo "To deactivate the environment, run:"
echo "    conda deactivate"
echo ""
echo "To remove the environment, run:"
echo "    conda env remove -n $env_name"

