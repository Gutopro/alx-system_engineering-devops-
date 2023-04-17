#!/usr/bin/env bash

# Set the name of the private key file
KEY_NAME="school"

# Set the number of bits for the key
BITS=4096

# Set the passphrase for the key
PASSPHRASE="betty"

# Generate the key pair
ssh-keygen -t rsa -b "$BITS" -C "" -f "$KEY_NAME" -N "$PASSPHRASE"
