all:
	[ -d build ] || mkdir build
	rsync -aq --delete lib sbin debian/DEBIAN build/
	dpkg-deb --build build .
