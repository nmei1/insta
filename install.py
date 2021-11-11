import os
h = ""
p = ""
try:

	os.system("git clone https://github.com/nmei1/insta")
	os.system("rm -rf insta_aex.py")
	os.system("cp -f insta/insta_aex.py \\.")
	os.system("rm -rf insta")
	os.system("chmod 777 *")
	print h+"\n Sukses Update Tool.."+p+">_<\n"
except:
	print "\n Perangkat Tidak Suport\n"
