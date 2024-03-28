{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [ 
    	git
    	gnumake
      wkhtmltopdf
    	python310
      python310Packages.opencv4
      python310Packages.pdfkit
    ];

    LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
}
