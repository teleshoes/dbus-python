Name:          python2-dbus
BuildArch:     aarch64
Version:       1.2.8
Release:       sf0.1
License:       Custom (open source, permissive)
Group:         Development/Libraries/Python
Summary:       D-Bus Python 2 Bindings
Distribution:  SailfishOS 4.3.0.12

Provides:      dbus-python=1.2.8-sf0.1
Provides:      python-dbus=1.2.8-sf0.1
Provides:      python2-dbus=1.2.8-sf0.1
Provides:      python2-dbus(aarch-64) = 1.2.8-sf0.1
Provides:      python2.7dist(dbus-python) = 1.2.8
Provides:      python2dist(dbus-python) = 1.2.8

Requires:      python2
Requires:      dbus
Requires:      libc.so.6()(64bit)
Requires:      libc.so.6(GLIBC_2.17)(64bit)
Requires:      libdbus-1.so.3()(64bit)
Requires:      libdbus-1.so.3(LIBDBUS_1_3)(64bit)
Requires:      libglib-2.0.so.0()(64bit)

%description
D-Bus python 2 bindings for use with python programs.

%files
%attr(0644, root, root) "/usr/include/dbus-1.0/dbus/dbus-python.h"
%attr(0644, root, root) "/usr/lib/pkgconfig/dbus-python.pc"
%attr(0644, root, root) "/usr/lib64/python2.7/site-packages/_dbus_bindings.la"
%attr(0755, root, root) "/usr/lib64/python2.7/site-packages/_dbus_bindings.so"
%attr(0644, root, root) "/usr/lib64/python2.7/site-packages/_dbus_glib_bindings.la"
%attr(0755, root, root) "/usr/lib64/python2.7/site-packages/_dbus_glib_bindings.so"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/__init__.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/__init__.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/__init__.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_compat.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_compat.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_compat.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_dbus.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_dbus.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_dbus.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_expat_introspect_parser.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_expat_introspect_parser.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/_expat_introspect_parser.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/bus.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/bus.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/bus.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/connection.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/connection.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/connection.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/decorators.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/decorators.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/decorators.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/exceptions.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/exceptions.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/exceptions.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gi_service.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gi_service.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gi_service.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/glib.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/glib.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/glib.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gobject_service.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gobject_service.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/gobject_service.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/lowlevel.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/lowlevel.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/lowlevel.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/__init__.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/__init__.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/__init__.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/glib.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/glib.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/mainloop/glib.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/proxies.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/proxies.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/proxies.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/server.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/server.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/server.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/service.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/service.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/service.pyo"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/types.py"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/types.pyc"
%attr(0644, root, root) "/usr/lib/python2.7/site-packages/dbus/types.pyo"
