RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

package:
	@mkdir -p build
	@date --utc +%Y%m%d%H%M%S > VERSION
	@${RPMBUILD} --define "_version %(cat VERSION)" -ba python3-rockit-common.spec
	@mv build/noarch/*.rpm .
	@rm -rf build VERSION

install:
	@date --utc +%Y%m%d%H%M%S > VERSION
	@python3 -m build --outdir .
	@sudo pip3 install rockit.common-$$(cat VERSION)-py3-none-any.whl
	@rm VERSION
