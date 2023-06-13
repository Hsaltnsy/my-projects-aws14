#!/bin/bash
#
# This script creates a new user on the local system.
# You will be prompted to enter the username (login), the person name, and a password.
# The username, password, and host for the account will be displayed.

# Make sure the script is being executed with superuser privileges.
if [[ $UID -ne 0 ]]
then 
        echo "Please run this script with superuser privilages"
        exit 1
fi
# Get the username (login).
read -p "Please enter your username: " username
# Get the real name (contents for the description field).
read -p "Please enter your real name: " real_name
# Get the password.
read -sp "Please enter your password: " password
# Create the account.
useradd -c $real_name -m $username 2> /dev/null
# Check to see if the useradd command succeeded.
if [[ $? -ne 0 ]] 
then
        echo -e "Failed to create the user!"
        exit 1
fi
# We don't want to tell the user that an account was created when it hasn't been.

# Set the password.
echo $password | passwd --stdin $username
# Check to see if the passwd command succeeded.
if [[ $? -ne 0 ]]
then
        echo -e "Failed to change password!"
        exit 1
fi
# Force password change on first login.
passwd -e $username
# Display the username, password, and the host where the user was created.
echo -e "$username\n"
echo -e "$real_name\n"
echo -e "$password"
# If you get bad interpreter error: "sed -i -e 's/\r$//' <script_name>" command first.