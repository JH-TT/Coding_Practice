{ pkgs, legacyPolygott }: {
	deps = [
		pkgs.bashInteractive
		pkgs.inotify-tools
	] ++ legacyPolygott;
}