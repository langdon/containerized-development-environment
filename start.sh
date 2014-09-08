#!/bin/bash

__create_user() {
# Create a user to SSH into as.
SSH_USER=lwhite
useradd $SSH_USER
SSH_USERPASS=newpass
echo -e "$SSH_USERPASS\n$SSH_USERPASS" | (passwd --stdin $SSH_USER)
echo ssh $SSH_USER password: $SSH_USERPASS
}

# Call all functions
__create_user
