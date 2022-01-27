file1 = open('requirements.txt', 'r')
lines = file1.readlines()

file2 = open('pip3_install_packages.sh', 'w')

for line in lines:
    file2.writelines("pip3 install "+line)

file2.close()
file1.close()
