RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

package:
	mkdir -p build
	${RPMBUILD} -ba python34-warwick-observatory-common.spec
	mv build/noarch/*.rpm .
	rm -rf build

