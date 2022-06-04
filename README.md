#disable ALSR
sudo bash -c 'echo 0 > /proc/sys/kernel/randomize_va_space'

#install gcc for 32bit
sudo apt install gcc-multilib g++-multilib
