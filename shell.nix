{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
    	git
    	gnumake
    	python39
    ];

    LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
}
