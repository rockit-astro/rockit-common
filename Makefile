RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

package:
	mkdir -p build
	${RPMBUILD} -ba python3-warwickobservatory.spec
	mv build/noarch/*.rpm .
	rm -rf build

