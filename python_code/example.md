python3 main.py --router 172.31.1.10 --username dranser --password cisco --threshold 1 --coefficient 0.8

sudo ip route add 192.168.254.0/24 via 172.31.1.254
sudo ping -f -s 56500 192.168.254.2
