#!/bin/bash
IP_ARG=$(hostname -I)
python3 ./chat_init.py $IP_ARG
