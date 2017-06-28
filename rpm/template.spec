Name:           ros-lunar-realtime-tools
Version:        1.10.0
Release:        0%{?dist}
Summary:        ROS realtime_tools package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/realtime_tools
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy

%description
Contains a set of tools that can be used from a hard realtime thread, without
breaking the realtime behavior. The tools currently only provides the realtime
publisher, which makes it possible to publish messages to a ROS topic from a
realtime thread. We plan to add a basic implementation of a realtime buffer, to
make it possible to get data from a (non-realtime) topic callback into the
realtime loop. Once the lockfree buffer is created, the realtime publisher will
start using it, which will result in major API changes for the realtime
publisher (removal of all lock methods).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Jun 28 2017 Stuart Glaser <sglaser@willowgarage.com> - 1.10.0-0
- Autogenerated by Bloom

* Tue Mar 21 2017 Stuart Glaser <sglaser@willowgarage.com> - 1.9.2-0
- Autogenerated by Bloom

